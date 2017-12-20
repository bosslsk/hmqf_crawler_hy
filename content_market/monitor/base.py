# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午4:16

author @heyao
"""

from content_market.utils.log import get_logger


class BaseMonitor(object):
    def __init__(self, queue, scheduler=None, *args, **kwargs):
        self.queue = queue
        self.scheduler = scheduler
        log_name = kwargs.pop('log_name', __name__)
        log_level = kwargs.pop('log_level', 'INFO')
        format_str = kwargs.pop('format_str', None)
        filename = kwargs.pop('filename', None)
        self.logger = get_logger(log_name, log_level, format_str, filename)

    def open(self):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()
