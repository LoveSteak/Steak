from .Project import Project
from .Server import Server
from .Validator import Validator
from .Logger import Logger
import importlib
from .Settings import BANNER,LOGLEVEL
import logging

class Steak:
    '''
    The Steak class is the core of the Steak(as you can see from its name)
    it gathers loaded projects together,runs all handlers background,and launch the HTTP server
    '''
    projects=[]
    
    
    def __init__(self):
        self.logger = Logger()
        self.logger.setLevel(LOGLEVEL)
        self.logger.banner(BANNER,"none")
        self.logger.info(f'Steak init')
        self.handlerlist=[]

    def add_project(self,project)->None:
        '''
        This function adds a project object passed in to the project list of this Steak object
        '''
        Validator(project,Project)
        self.projects.append(project)
        self.logger.info(f'Project {project.project_name} Loaded')

    def set_log_level(self,level):
        '''
        This function allows users to set their own log level
        You can use DEBUG INFO ERROR and so on supported by logging as its parameter
        '''
        self.logger.setLevel(getattr(logging,level))

    def run(self,ip:str,port:int,callbackpath:str="/callback",sslpem=None,sslkey=None)->None:
        '''
        This function launch a server implemented by Server class and start all handlers registered by add_handler function
        '''
        Validator(port,int)
        self.server=Server(ip,port,self.projects,callbackpath,sslpem,sslkey)
        server_thread=self.server.run_thread()
        for handler in self.handlerlist:
            handler.run_background()
        
        self.logger.info(f'Steak init finished\n\n')
        try:
            server_thread.join()
        except KeyboardInterrupt:
            self.logger.error(f'Receive KeyboardInterrupt. Steak is Exiting.')
            exit(0)

    def add_handler(self,handlername:str,*args,**kwargs):
        '''
        This function imports handler and append it to handlerlist
        '''
        handler=getattr(importlib.import_module(f'steak.handlers.{handlername}'),handlername)(*args,**kwargs)
        handler.set_steak(self)
        self.handlerlist.append(handler)
        #handler.run_background()