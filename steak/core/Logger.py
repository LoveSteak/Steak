import logging
from colorama import Fore, Style
import sys

class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger(name="Steak")
        
        if not self.logger.handlers:
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.DEBUG)
            self.logger.addHandler(ch)

    def type2symbol(self, typein):
        type2symbol_dict = {'normal': '[*] ',
            'bad': '[-] ', 'good': '[+] ', 'none': ''}

        return type2symbol_dict.get(typein, "[*] ")

    def setLevel(self,level):
        self.logger.setLevel(level)

    def getLevel(self):
        return self.logger.level

    def debug(self, msg, typein="normal"):
        self.logger.debug(Fore.WHITE + self.type2symbol(typein) +
                          str(msg) + Style.RESET_ALL)

    def info(self, msg, typein="normal"):
        self.logger.info(Fore.GREEN + self.type2symbol(typein) +
                         str(msg) + Style.RESET_ALL)

    def good(self, msg, typein="good"):
        self.logger.info(Fore.MAGENTA + self.type2symbol(typein) +
                         str(msg) + Style.RESET_ALL)

    def banner(self, msg, typein="none"):
        self.logger.info(Fore.YELLOW + self.type2symbol(typein) + str(msg) + Style.RESET_ALL)
        
    def warning(self, msg, typein="bad"):
        self.logger.warning(Fore.RED + self.type2symbol(typein) + str(msg) + Style.RESET_ALL)
        
    def error(self, msg, typein="bad"):
        self.logger.error(Fore.RED + self.type2symbol(typein) + str(msg) + Style.RESET_ALL)
        
    def critical(self, msg, typein="normal"):
        self.logger.critical(Fore.RED + self.type2symbol(typein) + str(msg) + Style.RESET_ALL)
