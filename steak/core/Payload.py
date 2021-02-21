from steak.utils.randstring import randstring
from steak.utils import steak_format, steakformat
class Payload:
    def __init__(self,payload_str,module) -> None:
        self.module=module
        self.taskid=randstring()
        self.payload_str=steak_format(payload_str,taskid=self.taskid)
    
    def set_client(self,client):
        self.client=client