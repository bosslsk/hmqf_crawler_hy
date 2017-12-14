# -*- coding: utf-8 -*-
"""
create on 2017-11-24 上午11:42

author @heyao
"""

from content_market.parser.qidian import Qidian

qidian = Qidian()

parser_dict = dict(
    Qidian=qidian
)


def parse(html, url, parser, parse_func):
    parser = parser_dict.get(parser, None)
    if not parser:
        return None
    if not hasattr(parser, parse_func):
        raise RuntimeError("%s object has no attribute %s" % (parser, parse_func))
    parse_func = getattr(parser, parse_func)
    return parse_func(html, url)
