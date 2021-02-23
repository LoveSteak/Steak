from steak.core import Project

class DemoProject(Project):
    def __init__(self) -> None:
        super().__init__()
        print('Demo project init..')
        self.jsurl='/jquery.js'
        
    def fuckhiram(self,client,result):
        print(result)
        alert=self.load_module('Alert',content='fuck hiram again')
        client.send_payload(alert)

    def attack_client(self,client:object):
        if 3>2:
            alert=self.load_module('Alert',content='fuck hiram')
            taskid=client.send_payload(alert,'fuck')
            result=None
            #result=client.send_payload(alert)
            #i+=1
            #print(result)
        return

    def on_metasploithandler(self,session):
        print("I'm so fucking lovvve msf")
        print(session)    
        self.stop_attack()

    def on_cobaltstrikehandler(self,session):
        print("I'm so fucking lovvve cobaltstrike")
        print(session)    
        #self.stop_attack()
    