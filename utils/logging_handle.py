# -*- coding:utf-8 -*-
import logging
import datetime
from configs.dir_path import logs_path
import os


def logging_handle(logFile=True, name=__name__):
    log_dir = os.path.join(logs_path, f"{datetime.datetime.now().strftime('%Y%m%d')}.log")
    logger = logging.getLogger(name)  # 创建日志器对象
    logger.setLevel(logging.INFO)  # 设置日志级别
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s [%(lineno)d]:%(message)s')  # 设置日志格式
    if logFile:
        file = logging.FileHandler(filename=log_dir, encoding='utf-8')  # 控制日志输出到文件
        file.setFormatter(fmt)
        logger.addHandler(file)
    else:
        console = logging.StreamHandler()  # 控制日志输出到控制台
        console.setFormatter(fmt)
        logger.addHandler(console)
    return logger


log = logging_handle()

