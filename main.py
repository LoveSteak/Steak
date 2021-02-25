import steak.core as Core
from DemoProject import DemoProject

if __name__=='__main__':
    steak=Core.Steak()
    steak.add_project(DemoProject())
    steak.add_handler("CobaltStrikeHandler")
    steak.run(ip='coderunnerapp.com',port=60000,callbackpath='/callback')