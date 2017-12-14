# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午12:20

author @heyao
"""


import json

import redis

from hm_collections.queue.redis_queue import RedisSetQueue

from content_market.checker.key_inject import inject
from content_market.scheduler import Scheduler
from content_market.parser import Qidian
from content_market.utils.pool import redis_connection_pool
from content_market.bin.url_check import ccc

r = redis.StrictRedis(connection_pool=redis_connection_pool)
queue = RedisSetQueue(r, 'spider:parse:chapter', json)
scheduler = Scheduler(r, "spider:html", RedisSetQueue, 'json')

qidian = Qidian(log_level="DEBUG")
while 1:
    data = queue.pop()
    if data:
        html = data['html']
        url = data['url']
        url_type = data['url_type']
        chapter_list = qidian.parse_chapter_list(html, url)
        for chapter in chapter_list:
            chapter_request_data = data['config']
            chapter_request_data = {k: inject(chapter_request_data[k], **chapter) for k in chapter_request_data}
            chapter_request_data['url'] = chapter_request_data['data_url']
            if chapter_request_data:
                chapter_request_data['url_type'] = 'content'
                print chapter_request_data
                scheduler.schedul(chapter_request_data)
            else:
                print 'no chapter'
