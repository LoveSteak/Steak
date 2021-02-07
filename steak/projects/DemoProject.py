from .Project import Project
class DemoProject(Project):
    def __init__(self) -> None:
        super().__init__()
        print('Demo project init..')

    def check_client(self,client:object):
        print('DemoProject Checking')
        return True
    
    def attack_client(self,client:object):
        print('DemoProject pwning!')
        print('Pwned!')
        return

    