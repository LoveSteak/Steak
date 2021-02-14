import importlib
class Project:
    def __init__(self) -> None:
        print('project init')
        self.clients={}
        self.jsurl='/jquery.js'
        pass
    
    def attack_client(self,client:object):
        return
    
    def load_module(self,modulename:str,*args,**kwargs):
        moduleobj=getattr(importlib.import_module(f'steak.modules.{modulename}.module'),modulename)
        return moduleobj(*args,**kwargs)
