from .Server import Server
class Steak:
    projects=[]
    def __init__(self) -> None:
        print('fuckhiram')
    def add_handler(self,handler:object)->None:
        print('add_handler...')
    def add_project(self,project:object)->None:
        print('add_project...')
        self.projects.append(project)
    def run(self,ip:str,port:int,callbackpath:str="/callback"):
        print(f'running at http://{ip}:{port}/')
        server=Server(ip,port,self.projects,callbackpath)
        server.run()