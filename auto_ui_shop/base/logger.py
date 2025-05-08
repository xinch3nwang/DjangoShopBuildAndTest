import logging
import os
from logging.handlers import TimedRotatingFileHandler
import gzip
import shutil
from pathlib import Path


def setup_logger():
    # 创建logs目录（自动创建，不存在时）
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'auto_ui_test.log')

    # 定义日志格式（包含时间、级别、模块、函数、行号、消息）
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(module)s:%(funcName)s:%(lineno)d - %(message)s'
    )

    # 控制台处理器（输出INFO及以上级别）
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(module)s:%(funcName)s:%(lineno)d - %(message)s'
    )
    console_handler.setFormatter(formatter)
    # 修改为INFO级别
    console_handler.setLevel(logging.INFO)

    # 文件处理器（按天滚动，保留7天日志，UTF-8编码）
    file_handler = TimedRotatingFileHandler(
        log_file,
        when='midnight',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    # 修改为INFO级别
    file_handler.setLevel(logging.INFO)

    # 初始化根日志器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # 全局最低级别为DEBUG
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # 压缩旧日志文件
    def compress_logs():
        for filename in os.listdir(log_dir):
            if filename.endswith('.log') and filename != 'auto_ui_test.log':
                with open(os.path.join(log_dir, filename), 'rb') as f_in:
                    with gzip.open(os.path.join(log_dir, filename + '.gz'), 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(os.path.join(log_dir, filename))

    # 每天压缩一次旧日志
    file_handler.suffix = "%Y-%m-%d.log"
    file_handler.namer = lambda name: name.replace(".log", "") + ".log"
    file_handler.rotator = compress_logs

    return logger

# 初始化日志配置（全局仅执行一次）
logger = setup_logger()