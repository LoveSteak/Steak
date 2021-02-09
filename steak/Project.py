class Project:
    def __init__(self) -> None:
        print('project init')
        self.clients={}
        self.jsurl='/jquery.js'
        pass
    
    def attack_client(self,client:object):
        return
    
    def load_module(self,modulename):
        __import__(f'../modules/{modulename}/{modulename}')
    
