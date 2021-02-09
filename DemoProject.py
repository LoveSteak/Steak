import steak.Project as Project
from steak.modules.Alert import Alert

class DemoProject(Project):
    def __init__(self) -> None:
        super().__init__()
        print('Demo project init..')
        self.jsurl='/jquery.js'
        
    
    def attack_client(self,client:object):
        alert=Alert(content=1145141919810).payload
        result=client.sendPayload(alert)
        print('DemoProject pwning!')
        print(result)
        return

    def OnMetasploitHandler(self,session):
        print("I'm so fucking lovvve msf")
        print(session)    
        alert=Alert(content='You Are Hacked!').payload
        for clientid in self.clients:
            client=self.clients[clientid]
            client.sendPayload(alert)
