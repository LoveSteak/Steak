from steak.core import Project

class DemoProject(Project):
    def __init__(self) -> None:
        super().__init__()
        print('Demo project init..')
        self.jsurl='/jquery.js'
        
    
    def attack_client(self,client:object):
        alert=self.load_module('Alert',content=1145141919810)
        result=client.send_payload(alert)
        print('DemoProject pwning!')
        print(result)
        return

    def on_metasploithandler(self,session):
        print("I'm so fucking lovvve msf")
        print(session)    
        alert=self.load_module('You are hacked',content=1145141919810)
        for clientid in self.clients:
            client=self.clients[clientid]
            client.send_payload(alert)
