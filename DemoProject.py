import steak.Project as Project
from steak.modules.Alert import Alert

class DemoProject(Project):
    def __init__(self) -> None:
        super().__init__()
        print('Demo project init..')
        self.jsurl='/jquery.js'

    def check_client(self,client:object):
        print('DemoProject Checking')
        return True
    
    def attack_client(self,client:object):
        alert=Alert(content=1145141919810)
        client.sendPayload(alert)
        print('DemoProject pwning!')
        print('Pwned!')
        return

    
