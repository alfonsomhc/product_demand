# logger.py

import logging

default_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
base_name = "main"


def get_logger(name=base_name, format=default_format):
    """
    Set up a stream logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(format)
    stream_handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(stream_handler)
    return logger
