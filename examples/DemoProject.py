from steak.core import Project

class DemoProject(Project):
    def __init__(self) -> None:
        super().__init__()
        self.project_name='demo project'
        self.jsurl='/jquery.js'

    def attack_client(self,client:object):
        alert=self.load_module('Alert',content='Hello World')
        client.send_payload(alert)
        self.stop_attack()
        return

    def on_metasploithandler(self,session):
        print("I'm so lovvve msf")
        print(session)    
        self.stop_attack()

    def on_cobaltstrikehandler(self,session):
        print("I'm so lovvve cobaltstrike")
        print(session)    
        self.stop_attack()
    