from abc import abstractmethod
import _thread
class Handler:
    '''
    The Handler class is the base class for external event handler.
    Users can derive this class to receive external events they care e.g. an online signal in CobaltStrike 
    Users should at least implement generate_event function to implement this class
    '''
    def __init__(self,callbackname=None) -> None:
        if callbackname:
            self.callbackname=callbackname
        else:
            self.callbackname="on_"+self.__class__.__name__.lower()

    def set_steak(self,steakobj)->str:
        self.steak=steakobj

    def get_callback_name(self)->str:
        return self.callbackname

    @abstractmethod
    def generate_event(self):
        '''
        Generates a single external event
        This function should be implemented by user and it should return only when an external event happened
        '''
        pass

    def run(self)->None:
        '''
        Continously calls the generate_event function to obtain an external event and calls callback functions corresponding to this handler in all projects
        '''
        while True:
            event=self.generate_event()
            for project in self.steak.projects:
                try:
                    method=getattr(project, self.callbackname)
                    #method(event)
                    _thread.start_new_thread( method, (event,))
                except:
                    continue
    
    def run_background(self)->None:
        '''
        Runs the self.run function in a new thread
        '''
        print('[*]Handler running background...')
        _thread.start_new_thread( self.run, tuple())
