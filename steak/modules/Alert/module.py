from steak.core.Module import Module

class Alert(Module):
    '''
    A simple demo module that alerts to the user
    '''
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        print('alert called!')