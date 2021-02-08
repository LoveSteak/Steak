from steak.Client import Client
from flask import Flask,Response,request
import uuid
import os
import json
from .utils import uniquerandstring
from .utils import base64decode,base64encode
class Server:
    def __init__(self,ip,port,projects,callbackpath) -> None:
        print('fuckserver')
        self.ip=ip
        self.port=port
        self.projects=projects
        self.callbackpath=callbackpath
        self.jsurl2projects={}
        self.clientid2client={}
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

    def run(self):
        print('server run run run ')
        app = Flask(__name__)
        app.config['SESSION_TYPE'] = 'filesystem'


        @app.route(self.callbackpath,methods=['GET','POST'])
        def callbackpath():
            # if 'jsurl' not in session: #check if new client 
            #     client=self._createclient(self.jsurl2projects[request.args.get("jsurl")])
            #     session['jsurl']= request.args.get("jsurl")
            #     session['clientid']=client.clientid
            #     self.clientid2client[client.clientid]=client 
            # client=self.clientid2client[session['clientid']]
            content=json.loads(base64decode(request.form.get('content')))
            clientid=content['clientbasicinfo']['clientid']
            project=self.jsurl2projects[content['clientbasicinfo']['jsurl']]
            dataupload=content['dataupload']
            if clientid not in self.clientid2client:
                client=Client(clientid,project,dataupload)
                self.clientid2client[clientid]=client
            else:
                client=self.clientid2client[clientid]
            resp=Response('fuck off')
            resp.headers['Access-Control-Allow-Origin'] ='*'
            return resp
            

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