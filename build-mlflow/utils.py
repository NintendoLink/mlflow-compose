import os
import logging
from functools import wraps


def get_abs_path(relative_path):

    '''将相对路径转换为绝对路径
        relative_path = './cache-model'
        transfer_relative_to_abs(relative_path)
    '''

    if os.path.isabs(relative_path):
        return relative_path
    abs_path = os.path.abspath(relative_path)
    return abs_path


def singleton(cls):

    '''Impl singleton mode via decorator'''
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):

        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return get_instance


@singleton
class Log:
    '''日志'''
    def __init__(self,log_name=None):

        self.log_name = log_name if log_name else 'generic-log'

        self._init()

    def _init(self):
        '''初始化logger对象'''
        self.logger = self.init_console_logger()

    def init_console_logger(self):
        # 1、logging
        # 1.1、logger
        logger = logging.getLogger(self.log_name)
        logger.setLevel(logging.DEBUG)

        # stream handler & file handler & logging formart
        sc = logging.StreamHandler()
        sc.setLevel(logging.DEBUG)

        # 1.2、时间、脚本名称、行号、级别、信息
        sc_formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s")
        sc.setFormatter(sc_formatter)

        # 1.3、add handler
        logger.addHandler(sc)
        return logger


if __name__ == '__main__':
    log = Log()
    log.logger.info("zhangsan")