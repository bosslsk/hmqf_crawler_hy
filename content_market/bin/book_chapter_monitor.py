# -*- coding: utf-8 -*-
"""
create on 2017-12-14 下午6:05

author @heyao
"""

import json
import redis
from hm_collections.queue.redis_queue import RedisSetQueue

from content_market.monitor.parser_monitor import BookChapterMonitor
from content_market.utils.pool import redis_connection_pool
from content_market.scheduler import Scheduler

r = redis.StrictRedis(connection_pool=redis_connection_pool)
queue = RedisSetQueue(r, 'spider:parse:chapter', json)
scheduler = Scheduler(r, 'spider:html', RedisSetQueue, 'json')
book_chapter_monitor = BookChapterMonitor(queue, scheduler, log_level="DEBUG")
book_chapter_monitor.run()
