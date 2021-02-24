from steak.utils.randstring import randstring
from steak.utils import steak_format, steakformat
from .Module import Module
from .Client import Client
class Payload:
    '''
    The Payload class stores the payload string that be sent to the client,the module and taskid and client it corresponds to.
    '''
    def __init__(self,payload_str:str,module:Module) -> None:
        self.module=module
        self.taskid=randstring()
        self.payload_str=steak_format(payload_str,taskid=self.taskid)
    
    def set_client(self,client:Client)->Client:
        self.client=client