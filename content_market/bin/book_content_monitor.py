# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午6:26

author @heyao
"""

from content_market.monitor.warm import WarmMonitor
from content_market.parser import parse


class BookContentMonitor(WarmMonitor):
    def __init__(self, queue, scheduler=None, *args, **kwargs):
        super(BookContentMonitor, self).__init__(queue, scheduler, *args, **kwargs)

    def one_step(self, data):
        html = data['html']
        url = data['url']
        url_type = data['url_type']
        config = data['config']
        parser = config['parser']
        parse_func = config['parse_func']

        content = parse(html, url, parser, parse_func)
        print content


if __name__ == '__main__':
    import json
    import redis
    from hm_collections.queue.redis_queue import RedisSetQueue
    from content_market.utils.pool import redis_connection_pool

    r = redis.StrictRedis(connection_pool=redis_connection_pool)
    queue = RedisSetQueue(r, 'spider:parse:content', json)
    book_content_monitor = BookContentMonitor(queue)
    book_content_monitor.run()
