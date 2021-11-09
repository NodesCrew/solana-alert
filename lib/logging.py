# coding: utf-8
import os
import config
import logging

os.makedirs(config.DIR_LOGS, exist_ok=True)


def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)8s] - %(name)16s - %(message)s")

        log_handler = logging.FileHandler(config.DIR_LOGS + "/%s.log" % name)
        log_handler.setFormatter(formatter)
        log_handler.setLevel(logging.DEBUG)
        logger.addHandler(log_handler)

        log_handler = logging.StreamHandler()
        log_handler.setFormatter(formatter)
        log_handler.setLevel(logging.DEBUG)
        logger.addHandler(log_handler)

        logger.setLevel(logging.DEBUG)
    return logger
