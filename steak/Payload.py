from steak.utils.randstring import randstring
class Payload:
    def __init__(self,payload_str,module) -> None:
        self.module=module
        self.taskid=randstring()
        self.payload_str=payload_str.replace('<steak>taskid</steak>',self.taskid)
    
    def setClient(self,client):
        self.client=client