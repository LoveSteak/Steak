from steak.core.Module import Module

class Consolelog(Module):
    '''
    A simple demo module that make a console log to the user
    '''
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)