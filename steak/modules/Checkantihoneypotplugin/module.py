from steak.core.Module import Module

class Checkantihoneypotplugin(Module):
    '''
    A simple demo module that checks anti honeypot plugin
    (https://github.com/Monyer/antiHoneypot)
    '''
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)