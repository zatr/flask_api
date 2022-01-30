import logging
import os


def setup():
    logger = logging.getLogger(__name__)
    logger.setLevel("DEBUG")
    fmt = "%(asctime)s.%(msecs)03d %(levelname)s:%(module)s:%(funcName)s:[%(lineno)d] %(message)s"
    date_fmt = "%Y-%m-%d %H:%M:%S"
    log_format = logging.Formatter(fmt, datefmt=date_fmt)
    con_handler = logging.StreamHandler()
    con_handler.setFormatter(log_format)
    logger.addHandler(con_handler)
    log_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log_file.txt')
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)


log = logging.getLogger(__name__)
