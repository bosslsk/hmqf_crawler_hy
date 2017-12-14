# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午4:16

author @heyao
"""


class BaseMonitor(object):
    def __init__(self, queue, scheduler=None, *args, **kwargs):
        self.queue = queue
        self.scheduler = scheduler

    def open(self):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()
