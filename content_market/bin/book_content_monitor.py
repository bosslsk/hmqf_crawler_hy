# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午6:26

author @heyao
"""

import json
import redis
from hm_collections.queue.redis_queue import RedisSetQueue
from content_market.utils.pool import redis_connection_pool
from content_market.monitor.parser_monitor import BookContentMonitor

r = redis.StrictRedis(connection_pool=redis_connection_pool)
queue = RedisSetQueue(r, 'spider:parse:content', json)
book_content_monitor = BookContentMonitor(queue, log_level="DEBUG")
book_content_monitor.run()
