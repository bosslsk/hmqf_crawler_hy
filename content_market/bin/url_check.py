# -*- coding: utf-8 -*-
"""
create on 2017-12-13 下午5:30

author @heyao
"""
import datetime
from copy import deepcopy

import redis

from content_market.checker import check_detail_url
from content_market.exceptions import HostNotSupportException
from content_market.scheduler import Scheduler
from content_market.utils.pool import redis_connection_pool, mongo

r = redis.StrictRedis(connection_pool=redis_connection_pool)
scheduler = Scheduler(r, 'spider:html', 'hm_collections.queue.redis_queue.RedisSetQueue', queue_serializer='json')


def add_url(url_info):
    url = url_info['url']
    support = True
    schedule = False
    try:
        request_data, config = check_detail_url(url)
    except HostNotSupportException:
        support = False
        return support, schedule
    data = deepcopy(request_data['extra'])
    data['added_at'] = datetime.datetime.now()
    result = mongo['book_index'].update_one(
        {'_id': '%s_%s' % (request_data['extra']['source'], request_data['extra']['book_id'])},
        {'$setOnInsert': data},
        upsert=True
    )
    if url_info.get('force_update', 0):
        scheduler.schedul(request_data)
        schedule = True
        return support, schedule
    elif not result.matched_count:
        scheduler.schedul(request_data)
        schedule = True
        return support, schedule
    return support, schedule


if __name__ == '__main__':
    urls = [
        {
            'url': 'https://book.qidian.com/info/1009704712',
            'force_update': 0
        },
        {
            'url': 'https://book.qidian.com/info/1007090207',
            'force_update': 0
        },
        {
            'url': 'http://www.hhh.com/info/1234567',
            'force_update': 0
        },
        {
            'url': 'http://www.shangshu.cc/99/99390/',
            'force_update': 1
        }
    ]
    for url_info in urls:
        support, schedule = add_url(url_info)
        if not support:
            print 'not support'
        elif schedule:
            print 'scheduled'
        else:
            print 'already have'
