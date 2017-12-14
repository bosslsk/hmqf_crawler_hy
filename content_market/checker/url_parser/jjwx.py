# -*- coding: utf-8 -*-
"""
create on 2017-12-14 上午9:48

author @heyao
"""
from content_market.checker.url_parser.utils import parse_url


def parse_jjwx(url):
    host, path, q = parse_url(url)
    book_id = q['novelid']
    extra_info = {'book_id': book_id, 'url': url}
    return host, path, extra_info


def parse_jjwx_chapter(url):
    host, path, q = parse_url(url)
    book_id = q['novelId']
    extra_info = {'book_id': book_id, 'url': url}
    return host, path, extra_info
