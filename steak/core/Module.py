from steak.core import Payload

class Module:
    def __init__(self,**kwargs) -> None:
        self.jstemplate=open('steak/modules/'+self.__class__.__name__+'/command.js').read()
        self.kwargs=kwargs
        self.jspayload=self.format_js(**self.kwargs)
        self.payload=self.get_jspayload()
    
    def format_js(self,**kwargs):
        ret=self.jstemplate
        for key in kwargs:
            ret=ret.replace(f"<steak>{str(key)}</steak>",str(kwargs[key]))
        return ret
    
    def get_jspayload(self):
        return Payload(self.jspayload,self)
    
    def parse_result(self,result):
        return result