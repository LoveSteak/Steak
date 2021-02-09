import steak.Payload as Payload

class Module:
    def __init__(self,**kwargs) -> None:
        self.jstemplate=open('steak/modules/'+self.__class__.__name__+'/command.js').read()
        self.kwargs=kwargs
        self.jspayload=self.formatJs(**self.kwargs)
        self.payload=self.getJsPayload()
    
    def formatJs(self,**kwargs):
        ret=self.jstemplate
        for key in kwargs:
            ret=ret.replace(f"<steak>{str(key)}</steak>",str(kwargs[key]))
        return ret
    
    def getJsPayload(self):
        return Payload(self.jspayload,self)
    
    def parseResult(self,result):
        return result