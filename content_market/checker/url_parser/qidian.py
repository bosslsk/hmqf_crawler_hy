# -*- coding: utf-8 -*-
"""
create on 2017-12-14 上午9:47

author @heyao
"""
from content_market.checker.url_parser.utils import parse_url


def parse_qidian(url):
    host, path, q = parse_url(url)
    book_id = path.split('/')[-1]
    extra_info = {'book_id': book_id, 'url': url}
    return host, path, extra_info
