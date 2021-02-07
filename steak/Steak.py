class Steak:
    def __init__(self) -> None:
        print('fuckhiram')
    def add_handler(self,handler:object)->None:
        print('add_handler...')
    def add_project(self,project:object)->None:
        print('add_project...')
    def run(self,ip:str,port:int):
        print(f'running at http://{ip}:{port}/')