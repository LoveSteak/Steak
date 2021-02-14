from pymetasploit3.msfrpc import MsfRpcClient
from steak.core.Handler import Handler
import copy
import _thread
import time

class MetasploitHandler(Handler):
    def __init__(self,password:str,port=55553,ssl=False) -> None:
        super().__init__()
        self.client = MsfRpcClient(password, ssl=False)

    def generate_event(self):
        last_sessions=copy.deepcopy(self.client.sessions.list)
        while True:
            time.sleep(1)
            print('[*]running generating msf event...')
            if len(self.client.sessions.list)>len(last_sessions):
                print('[+]Oh my god!!! Online!!!!')
                return self.client.sessions.list
            
    