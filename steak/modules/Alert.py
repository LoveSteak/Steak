from steak.Module import Module

class Alert(Module):
    def __init__(self,**kwargs) -> None:
        super().__init__(**kwargs)
        print('alert called!')