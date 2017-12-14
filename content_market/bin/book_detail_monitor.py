# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午5:43

author @heyao
"""
from content_market.bin.url_check import ccc
from content_market.checker.checker_settings import chapter_config
from content_market.monitor.warm import WarmMonitor
from content_market.parser import parse


class BookDetailMonitor(WarmMonitor):
    def __init__(self, queue, scheduler, *args, **kwargs):
        super(BookDetailMonitor, self).__init__(queue, scheduler, *args, **kwargs)

    def one_step(self, data):
        html = data['html']
        url = data['url']
        url_type = data['url_type']
        config = data['config']
        parser = config['parser']
        parse_func = config['parse_func']

        detail_info = parse(html, url, parser, parse_func)
        print detail_info
        chapter_request_data, config = ccc(url, chapter_config)
        if chapter_request_data:
            chapter_request_data['url_type'] = 'chapter'
            chapter_request_data['config'] = config
            print chapter_request_data
            self.scheduler.schedul(chapter_request_data)


if __name__ == '__main__':
    import json
    import redis
    from hm_collections.queue.redis_queue import RedisSetQueue
    from content_market.utils.pool import redis_connection_pool
    from content_market.scheduler import Scheduler

    r = redis.StrictRedis(connection_pool=redis_connection_pool)
    queue = RedisSetQueue(r, 'spider:parse:detail', json)
    scheduler = Scheduler(r, 'spider:html', RedisSetQueue, 'json')
    book_detail_monitor = BookDetailMonitor(queue, scheduler)
    book_detail_monitor.run()
