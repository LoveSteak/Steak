from queue import Queue
from pymetasploit3.msfrpc import MsfRpcClient
from steak.core.Handler import Handler
import copy
import time
import threading



class CobaltStrikeHandler(Handler):
    '''
    This is an implementation of a handler that recevies online event of CobaltStrike victim.
    Due to the fucking complexity of the protocol of CobaltStrike, we register a path to the Server class to receive information pushed by CobaltStrike server
    To use this handler, you need to deploy the cobaltstrike.cna in CobaltStrike Server and make sure they have identical "password" and the serverurl in the cna script is same to the one we registerd
    '''
    def callback_registedpath(self,request):
        '''
        Receives information pushed by CobaltStrike server
        if the password received is identical to the self.password, it set the onlineinfo in
        '''
        if request.form.get('password')==self.password:
            self.onlineinfo.put({'ip':request.form.get('ip'),'computername':request.form.get('computername'),'username':request.form.get('username')})
        return ''


    def __init__(self,listenonpath='/cobaltstrikecallback',password='fuckhiram') -> None:
        super().__init__()
        self.onlineinfo=Queue()
        self.lisenonpath=listenonpath
        self.password=password
        self.init=False

    def generate_event(self):
        if self.init==False:
            self.steak.server.register_path(self.lisenonpath,self.callback_registedpath)
            self.init=True
        return self.onlineinfo.get()
        
            
    