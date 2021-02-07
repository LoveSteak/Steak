class Project:
    def __init__(self) -> None:
        print('project init')
        pass
    
    def check_client(self,client:object):
        return True
    
    def attack_client(self,client:object):
        print('Pwned!')
        return

    