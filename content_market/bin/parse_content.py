# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午2:06

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
queue = RedisSetQueue(r, 'spider:parse:content', json)

qidian = Qidian(log_level="DEBUG")
while 1:
    data = queue.pop()
    if data:
        html = data['html']
        url = data['url']
        url_type = data['url_type']
        print qidian.parse_content(html)
