import json
class Client:
    def __init__(self,clientid,project,clientinfo) -> None:
        self.clientid=clientid
        self.project=project
        self.useragent=clientinfo['useragent']
        self.curdomaincookies=clientinfo['curdomaincookies']
        self.cururl=clientinfo['cururl']