# -*- coding: utf-8 -*-
"""
create on 2017-12-13 上午10:11

author @heyao
"""

import re


def query_config(config, **queries):
    """从列表的config中查询指定属性的配置
    :param config: list. 配置表
    :param queries: kwargs, 查询的值
    :return: dict. 查询到的配置
    """
    query_path = queries.pop('path', None)
    for c in config:
        if c.get('status', 1) == 0:
            continue
        path = c.pop('path', None)
        if path and query_path:
            reg = re.compile(path)
            if reg.match(query_path) and all(c[q] == queries[q] for q in queries):
                c['path'] = path
                return c
        elif all(c[q] == queries[q] for q in queries):
            c['path'] = path
            return c
    return {}


if __name__ == '__main__':
    from content_market.checker.checker_settings import hosts_config

    print query_config(hosts_config, **{'host': 'book.qidian.com', 'path': '/info/123456'})
