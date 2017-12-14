# -*- coding: utf-8 -*-
"""
create on 2017-12-13 下午2:40

author @heyao
"""

from urlparse import urlparse, parse_qs


def parse_url(url):
    p = urlparse(url)
    host = p.hostname
    path = p.path
    query = p.query
    q = parse_qs(query, keep_blank_values=1)
    q = {k: q[k][0] for k in q}
    return host, path, q
