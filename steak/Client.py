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
        self.taskresult={}

    def getlatesttask(self):
        try:
            return self.taskqueue.get(False)
        except:
            return None
    
    def sendPayload(self,payload,sync=1):
        payload.setClient(self)
        self.taskqueue.put(payload)
        taskid=payload.taskid
        while sync:
            time.sleep(1)
            if  taskid in self.taskresult:
                return self.taskresult[taskid]
        return taskid