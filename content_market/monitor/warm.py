# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午4:11

author @heyao
"""

import threading

import signal

import time

from content_market.monitor.base import BaseMonitor


class WarmMonitor(BaseMonitor):
    handle_SIGINT = 0

    def __init__(self, queue, scheduler=None, *args, **kwargs):
        super(WarmMonitor, self).__init__(queue, scheduler, *args, **kwargs)
        self.warm_stop = False  # if True, it will stop

    def open(self):
        signal.signal(signal.SIGINT, self.handle_signal)

    def handle_signal(self, signum, frame):
        if self.handle_SIGINT == 0:
            self.warm_stop = True
            self.handle_SIGINT += 1
            self.logger.info("Received SIGINT, send again to force shut down.")
        elif self.handle_SIGINT == 1:
            self.logger.info("Received SIGINT twice, program will shut down.")
            exit(0)

    def run(self, sleep_time=5, log=True):
        self.open()
        # condition = threading.Condition()
        if log:
            print "press Ctrl+C to quit."
        while 1:
            if self.warm_stop:
                break
            data = self.queue.pop()
            if data:
                self.one_step(data)
            else:
                # wait
                # condition.acquire()
                # condition.wait(sleep_time)
                time.sleep(sleep_time)

    def one_step(self, data):
        raise NotImplementedError()


if __name__ == '__main__':
    import sys

    import redis

    from hm_nlp.sentiments.word_freq import SentimentByWordFreq
    from hm_collections.queue.redis_queue import RedisSetQueue

    reload(sys)
    sys.setdefaultencoding('utf-8')

    r = redis.StrictRedis()
    key = 'test'
    queue_cls = RedisSetQueue
    queue = queue_cls(r, key)
    sentimentor = SentimentByWordFreq()


    class Monitor(WarmMonitor):
        def __init__(self, queue, scheduler=None, *args, **kwargs):
            super(Monitor, self).__init__(queue, scheduler, *args, **kwargs)
            self.logger.debug("ok")

        def one_step(self, data):
            with open(u'/Users/heyao/Desktop/novel/闪婚爱妻(2).txt', 'r') as f:
                content = f.read().decode('gbk')
            parts = [content[500 * i: 500 * (i + 1)] for i in range(len(content) / 500)]
            senti = []
            for p in parts:
                s = sentimentor.sentiment(p)['neg']
                senti.append(s)
            print len(senti)

    wm = Monitor(queue, log_name=__name__, log_level='DEBUG')
    wm.run()
