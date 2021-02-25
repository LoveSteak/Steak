from .Project import Project
from .Server import Server
from .Validator import Validator
from .Logger import Logger
import importlib



class Steak:
    '''
    The Steak class is the core of the Steak(as you can see from its name)
    it gathers loaded projects together,runs all handlers background,and launch the HTTP server
    '''
    projects=[]
    
    
    def __init__(self):
        self.logger = Logger(logger="Steak.py")
        banner='''
        
        ███████╗████████╗███████╗ █████╗ ██╗  ██╗
        ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║ ██╔╝
        ███████╗   ██║   █████╗  ███████║█████╔╝ 
        ╚════██║   ██║   ██╔══╝  ██╔══██║██╔═██╗ 
        ███████║   ██║   ███████╗██║  ██║██║  ██╗
        ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  v0.1 2021-01-25
                                                
        '''
        self.logger.info(banner)
        

    def add_project(self,project)->None:
        '''
        This function adds a project object passed in to the project list of this Steak object
        '''
        Validator(project,Project)
        self.projects.append(project)

    def run(self,ip:str,port:int,callbackpath:str="/callback")->None:
        '''
        This function launch a server implemented by Server class
        '''
        print(f'running at http://{ip}:{port}/')
        Validator(port,int)
        self.server=Server(ip,port,self.projects,callbackpath)
        self.server.run()

    def add_handler(self,handlername:str,*args,**kwargs):
        '''
        This function imports handler and run it
        '''
        handler=getattr(importlib.import_module(f'steak.handlers.{handlername}'),handlername)(*args,**kwargs)
        handler.set_steak(self)
        handler.run_background()
        print('add_handler...')

        