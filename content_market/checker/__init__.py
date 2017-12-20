# -*- coding: utf-8 -*-
"""
create on 2017-11-24 上午11:39

author @heyao
"""
from content_market.checker.checker_settings import hosts_config, chapter_config
from content_market.checker.query import query_config
from content_market.checker.url_parser import make_request_data, parse
from content_market.exceptions import HostNotSupportException


def _check(url, settings):
    try:
        host, path, extra_info = parse(url, settings)
    except HostNotSupportException:
        raise HostNotSupportException("host with path not support")
    config = query_config(settings, host=host, path=path)
    request_data = make_request_data(config, extra_info)
    request_data['extra'] = dict(**extra_info)
    return request_data, config


def check_detail_url(url, settings=hosts_config):
    request_data, config = _check(url, settings)
    request_data['url_type'] = 'detail'
    request_data['config'] = config
    return request_data, config


def check_chapter_url(url, settings=chapter_config):
    request_data, config = _check(url, settings)
    request_data['url_type'] = 'chapter'
    return request_data, config
