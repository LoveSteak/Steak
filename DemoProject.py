from steak.core import Project

class DemoProject(Project):
    def __init__(self) -> None:
        super().__init__()
        print('Demo project init..')
        self.jsurl='/jquery.js'
        
    
    def attack_client(self,client:object):
        i=0
        while True:
            alert=self.load_module('Consolelog',content=i)
            result=client.send_payload(alert)
            i+=1
            print(result)
        return

    def on_metasploithandler(self,session):
        print("I'm so fucking lovvve msf")
        print(session)    
        self.stop_attack()
