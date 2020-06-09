# 配置日志的格式
import logging
from logging import handlers

from utils import Utils


def basic_log_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 设置处理器
    sh = logging.StreamHandler()
    file_name = Utils.get_path() + "/log/homework.log"
    tf = logging.handlers.TimedRotatingFileHandler(filename=file_name, when="M", interval=1, backupCount=3,
                                                   encoding="utf-8")
    # 创建格式化器
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    sh.setFormatter(formatter)
    tf.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(tf)
