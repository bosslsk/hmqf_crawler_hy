# -*- coding: utf-8 -*-
"""
create on 2017-12-12 下午5:07

author @heyao
"""

import logging


def get_logger(name, log_level="INFO", format_str="[%(name)s][%(asctime)s] %(levelname)s: %(message)s", filename=None):
    format_str = format_str or "[%(name)s][%(asctime)s] %(levelname)s: %(message)s"
    logging.basicConfig(
        level=getattr(logging, log_level),
        format=format_str,
        filename=filename,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger(name)
    logger = logging.LoggerAdapter(logger, {})
    return logger


if __name__ == '__main__':
    logger = get_logger(__name__, log_level='DEBUG')
    logger.info("test")
    logger.debug("debug test")
