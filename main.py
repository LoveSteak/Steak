from steak.core import Steak
from steak.handlers.MetasploitHandler import MetasploitHandler
from DemoProject import DemoProject
if __name__=='__main__':
    steak=Steak()
    steak.add_project(DemoProject())
    steak.add_handler(MetasploitHandler(password='T56pKJIl',ssl=False))
    steak.run(ip='kali',port=666,callbackpath='/callback')