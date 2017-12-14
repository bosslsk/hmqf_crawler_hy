# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午6:05

author @heyao
"""

from content_market.checker.key_inject import inject
from content_market.monitor.warm import WarmMonitor
from content_market.parser import parse


class BookChapterMonitor(WarmMonitor):
    def __init__(self, queue, scheduler=None, *args, **kwargs):
        super(BookChapterMonitor, self).__init__(queue, scheduler, *args, **kwargs)

    def one_step(self, data):
        html = data['html']
        url = data['url']
        url_type = data['url_type']
        config = data['config']
        parser = config['parser']
        parse_func = config['parse_func']

        chapter_list = parse(html, url, parser, parse_func)
        for chapter in chapter_list:
            chapter_request_data = data['config']
            chapter_request_data = {k: inject(chapter_request_data[k], **chapter) for k in chapter_request_data}
            if chapter_request_data:
                chapter_request_data['url_type'] = 'content'
                chapter_request_data['config'] = config['content_config']
                chapter_request_data['url'] = chapter_request_data['data_url']
                print chapter_request_data
                self.scheduler.schedul(chapter_request_data)


if __name__ == '__main__':
    import json
    import redis
    from hm_collections.queue.redis_queue import RedisSetQueue
    from content_market.utils.pool import redis_connection_pool
    from content_market.scheduler import Scheduler

    r = redis.StrictRedis(connection_pool=redis_connection_pool)
    queue = RedisSetQueue(r, 'spider:parse:chapter', json)
    scheduler = Scheduler(r, 'spider:html', RedisSetQueue, 'json')
    book_chapter_monitor = BookChapterMonitor(queue, scheduler)
    book_chapter_monitor.run()
