from pymetasploit3.msfrpc import MsfRpcClient
from steak.core.Handler import Handler
import copy
import time
import threading



class CobaltStrikeHandler(Handler):
    def callback_registedpath(self,request):
        if request.form.get('password')==self.password:
            self.onlineinfo={'ip':request.form.get('ip'),'computername':request.form.get('computername'),'username':request.form.get('username')}
            self.semaphore.release()
        return ''


    def __init__(self,listenonpath='/cobaltstrikecallback',password='fuckhiram') -> None:
        super().__init__()
        self.lisenonpath=listenonpath
        self.password=password
        self.init=False

    def generate_event(self):
        if self.init==False:
            self.steak.server.register_path(self.lisenonpath,self.callback_registedpath)
            self.init=True
        self.semaphore=threading.Semaphore(0)
        self.semaphore.acquire()
        return self.onlineinfo
        
            
    