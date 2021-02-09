from abc import ABCMeta, abstractmethod
import _thread
class Handler:
    def __init__(self,callbackname=None) -> None:
        if callbackname:
            self.callbackname=callbackname
        else:
            self.callbackname="On"+self.__class__.__name__
    def setSteak(self,steakobj):
        self.steak=steakobj

    def getCallbackname(self):
        return self.callbackname

    @abstractmethod
    def generateEvent(self):
        pass

    def run(self):
        while True:
            event=self.generateEvent()
            for project in self.steak.projects:
                try:
                    method=getattr(project, self.callbackname)
                    #method(event)
                    _thread.start_new_thread( method, (event,))
                except:
                    continue
    
    def run_background(self):
        print('[*]Handler running background...')
        _thread.start_new_thread( self.run, tuple())
