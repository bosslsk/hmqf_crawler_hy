# -*- coding: utf-8 -*-
"""
create on 2017-12-13 下午5:30

author @heyao
"""

import json

import requests

from content_market.exceptions import HostNotSupportException
from content_market.scheduler import Scheduler
from content_market.checker.checker_settings import hosts_config, chapter_config
from content_market.checker.key_inject import inject
from content_market.checker.url_parser import parse_jjwx
from content_market.checker.query import query_config
from content_market.checker.url_parser import parse, make_request_data


def aaa(url):
    host, path, extra_info = parse_jjwx(url)
    config = query_config(chapter_config, host=host, path=path)
    data_url = inject(config['data_url'], **extra_info)
    headers = config['headers']
    formdata = config['formdata']
    if headers:
        headers = {k: inject(headers[k], **extra_info) for k in headers}
    if formdata:
        formdata = {k: inject(formdata[k], **extra_info) for k in formdata}
    method = 'POST' if formdata is not None else 'GET'
    chapter_list = json.loads(requests.request(method, data_url, headers=headers, data=formdata).content)['chapterlist']
    content_config = config['content_config']
    for chapter in chapter_list:
        chapter = {'chapter_id': chapter['chapterid'], 'book_id': extra_info['book_id']}
        data_url = inject(content_config['data_url'], **chapter)
        formdata = content_config['formdata']
        headers = content_config['headers']
        if formdata:
            formdata = {k: inject(formdata[k], **chapter) for k in formdata}
        if headers:
            headers = {k: inject(headers[k], **chapter) for k in headers}
        method = 'POST' if formdata is not None else 'GET'
        content = requests.request(method, data_url, headers=headers, data=formdata).content
        print content


import redis
from content_market.utils.pool import redis_connection_pool

r = redis.StrictRedis(connection_pool=redis_connection_pool)
scheduler = Scheduler(r, 'spider:html', 'hm_collections.queue.redis_queue.RedisSetQueue', queue_serializer='json')


def bbb(url):
    try:
        host, path, extra_info = parse(url, hosts_config)
    except HostNotSupportException:
        print 'false'
        return False
    config = query_config(hosts_config, host=host, path=path)
    request_data = make_request_data(config, extra_info)
    request_data['url_type'] = 'detail'
    scheduler.schedul(request_data)
    print 'true'
    return True


def ccc(url, settings):
    try:
        host, path, extra_info = parse(url, settings)
    except HostNotSupportException:
        return False
    config = query_config(settings, host=host, path=path)
    request_data = make_request_data(config, extra_info)
    request_data['url_type'] = 'chapter'
    request_data['config'] = config['content_config']
    return request_data


if __name__ == '__main__':
    url = 'https://book.qidian.com/info/1009704712'
    bbb(url)
