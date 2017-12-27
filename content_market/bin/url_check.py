# -*- coding: utf-8 -*-
"""
create on 2017-12-13 下午5:30

author @heyao
"""
import datetime
from copy import deepcopy

import redis

from content_market.checker import UrlChecker, hosts_config, chapter_config
from content_market.scheduler import Scheduler
from content_market.utils.pool import redis_connection_pool, mongo

r = redis.StrictRedis(connection_pool=redis_connection_pool)
scheduler = Scheduler(r, 'spider:html', 'hm_collections.queue.redis_queue.RedisSetQueue', queue_serializer='json')
url_checker = UrlChecker(hosts_config, chapter_config)


def add_url(url, force_update):
    """
    :param url: str. full url, contain scheme, host, path, <query>
    :param force_update: bool. whether to force update. if True, it will update the data in the db 
    :return: 
    """
    schedule = False
    request_data, support = url_checker.add_url(url)
    if request_data is None:
        return support, schedule
    data = deepcopy(request_data['extra'])
    data['added_at'] = datetime.datetime.now()
    coll = mongo['book_index']
    result = coll.update_one(
        {'_id': '%s_%s' % (request_data['extra']['source'], request_data['extra']['book_id'])},
        {'$setOnInsert': data},
        upsert=True
    )
    if force_update:
        schedule = scheduler.schedul(request_data)
    elif not result.matched_count:
        schedule = scheduler.schedul(request_data)
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
            'url': 'http://www.shangshu.cc/99/99290/',
            'force_update': 0
        }
    ]
    for url_info in urls:
        url = url_info['url']
        force_update = url_info['force_update']
        support, schedule = add_url(url, force_update)
        if not support:
            print 'not support'
        elif schedule:
            print 'scheduled'
        else:
            print 'already have'
