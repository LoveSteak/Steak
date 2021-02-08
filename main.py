from steak import Steak
from steak.handlers import CobaltStrikeHandler
from steak.projects import DemoProject
if __name__=='__main__':
    steak=Steak()
    steak.add_handler(CobaltStrikeHandler(host='kali',password='1145141919810'))
    steak.add_project(DemoProject())
    steak.run(ip='kali',port=666,callbackpath='/callback')