'''
	
	Logger formatter, based on python logging module
	Author. Federico Marinelli


'''
import logging

class log:
	__shared_state = {}
	def __init__(self):
		self.__dict__ = self.__shared_state

	@classmethod
	def _get_logger(cls, level):
		logger = logging.getLogger("")
		stream_handler = logging.StreamHandler()
		formatter=cls._get_formatter(level)
		stream_handler.setFormatter(formatter)
		logger.handlers = []
		logger.addHandler(stream_handler)
		return logger

	@classmethod
	def _get_formatter(cls, level):
		if level == 4:
			return logging.Formatter('\033[1;37;40m%(asctime)s - |\033[1;37;42m   INFO   \033[1;37;40m| - \033[0;37;40m%(message)s')
		elif level == 1:
			return logging.Formatter('\033[1;37;40m%(asctime)s - |\033[1;37;41m   %(levelname)s  \033[1;37;40m| - \033[0;37;40m%(message)s')
		else:
			return logging.Formatter('\033[1;37;40m%(asctime)s - |\033[1;37;43m  %(levelname)s \033[1;37;40m| - \033[0;37;40m%(message)s')

	@classmethod
	def error(cls, message):
		logger = cls._get_logger(1)
		logger.error(message)

	@classmethod
	def info(cls, message):
		logger = cls._get_logger(4)
		logger.error(message)

	@classmethod
	def warning(cls, message):
		logger = cls._get_logger(2)
		logger.warning(message)

