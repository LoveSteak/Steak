from steak.core import Payload
from steak.utils import steak_format
class Module:
    def __init__(self,**kwargs) -> None:
        self.jstemplate=open('steak/modules/'+self.__class__.__name__+'/command.js').read()
        self.kwargs=kwargs
        self.jspayload=steak_format(self.jstemplate,**self.kwargs)
        self.payload=self.get_jspayload()

    
    def get_jspayload(self):
        return Payload(self.jspayload,self)
    
    def parse_result(self,result):
        return result