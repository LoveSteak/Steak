import steak.core as Core
from DemoProject import DemoProject

if __name__=='__main__':
    steak=Core.Steak()
    steak.set_log_level("INFO")
    steak.add_project(DemoProject())
    steak.add_handler("CobaltStrikeHandler")
    steak.run(ip='localhost.ptlogin2.qq.com',port=6600,callbackpath='/callback')