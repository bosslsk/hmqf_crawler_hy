# -*- coding: utf-8 -*-
"""
create on 2017-12-14 上午11:43

author @heyao
"""

import json

import redis

from hm_collections.queue.redis_queue import RedisSetQueue

from content_market.checker.checker_settings import chapter_config
from content_market.scheduler import Scheduler
from content_market.parser import Qidian
from content_market.utils.pool import redis_connection_pool
from content_market.bin.url_check import ccc

r = redis.StrictRedis(connection_pool=redis_connection_pool)
queue = RedisSetQueue(r, 'spider:parse:detail', json)
scheduler = Scheduler(r, "spider:html", RedisSetQueue, 'json')

qidian = Qidian(log_level="DEBUG")
while 1:
    data = queue.pop()
    if data:
        html = data['html']
        url = data['url']
        url_type = data['url_type']
        detail_info = qidian.parse_detail(html, url)
        print detail_info
        chapter_request_data = ccc(url, chapter_config)
        if chapter_request_data:
            chapter_request_data['url_type'] = 'chapter'
            print chapter_request_data
            scheduler.schedul(chapter_request_data)
        else:
            print 'no chapter'
