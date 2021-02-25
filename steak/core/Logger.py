import logging
from colorama import Fore, Style
import sys

class Logger(object):
	def __init__(self, logger):
		self.logger = logging.getLogger(name=logger)
		self.logger.setLevel(logging.DEBUG)  # 指定最低的日志级别 critical > error > warning > info > debug
		if not self.logger.handlers:
			# 创建一个handler，用于输出到控制台
			ch = logging.StreamHandler(sys.stdout)
			ch.setLevel(logging.DEBUG)
			
			# 定义handler的输出格式
#			formatter = logging.Formatter(
#				"%(asctime)s  - %(message)s")
#			ch.setFormatter(formatter)
			
			# 给logger添加handler
			# self.logger.addHandler(fh)
			self.logger.addHandler(ch)
	def debug(self, msg):
		self.logger.debug(Fore.WHITE + str(msg) + Style.RESET_ALL)
		
	def info(self, msg):
		self.logger.info(Fore.GREEN + str(msg) + Style.RESET_ALL)
		
	def warning(self, msg):
		self.logger.warning(Fore.RED + str(msg) + Style.RESET_ALL)
		
	def error(self, msg):
		self.logger.error(Fore.RED + str(msg) + Style.RESET_ALL)
		
	def critical(self, msg):
		self.logger.critical(Fore.RED + str(msg) + Style.RESET_ALL)