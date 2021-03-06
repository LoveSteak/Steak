from pymetasploit3.msfrpc import MsfRpcClient
from steak.core.Handler import Handler
import time


class MetasploitHandler(Handler):
    def __init__(self,password:str,port=55552,ssl=False) -> None:
        super().__init__()
        self.client = MsfRpcClient(password, port=port,ssl=False)
        

    def generate_event(self):
        '''
        Polls the msf server via msfrpc, returns when number of msf sessions increases.
        '''
        last_sessions=self.client.sessions.list
        while True:
            time.sleep(1)
            if len(self.client.sessions.list)>len(last_sessions):
                return self.client.sessions.list
            
    