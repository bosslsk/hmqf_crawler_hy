# -*- coding: utf-8 -*-
"""
create on 2017-12-14 上午9:46

author @heyao
"""

from content_market.exceptions import HostNotSupportException
from content_market.checker.key_inject import inject
from content_market.checker.query import query_config
from content_market.checker.url_parser.utils import parse_url
from content_market.checker.url_parser.qidian import parse_qidian
from content_market.checker.url_parser.jjwx import parse_jjwx
from content_market.checker.url_parser.shangshu import parse_shangshu

parse_dict = {
    'www.jjwxc.net': parse_jjwx,
    'book.qidian.com': parse_qidian,
    'www.shangshu.cc': parse_shangshu
}

source_dict = {
    '.qidian.': 1,
    '.jjwxc.': 7,
    '.shangshu.': 15
}


def parse(url, settings):
    host, path, _ = parse_url(url)
    config = query_config(settings, host=host, path=path)
    if not config:
        raise HostNotSupportException("host and path not support")
    parse_func = parse_dict[host]
    host, path, extra_info = parse_func(url)
    extra_info['source'] = [source_dict[k] for k in source_dict if k in host][0]
    return host, path, extra_info


def make_request_data(config, extra_info, **extra):
    """从配置生成request数据
    :param config: dict.
    :param extra_info: dict. 
    :param extra: kwargs.
    :return: 
    """
    # TODO: 添加额外的信息
    data_url = inject(config['data_url'], **extra_info)
    headers = config['headers']
    formdata = config['formdata']
    if headers:
        headers = {k: inject(headers[k], **extra_info) for k in headers}
    if formdata:
        formdata = {k: inject(formdata[k], **extra_info) for k in formdata}
    return {'url': data_url, 'headers': headers, 'formdata': formdata}


if __name__ == '__main__':
    from content_market.checker.checker_settings import hosts_config

    print parse('http://www.jjwxc.net/onebook.php?novelid=3425247', hosts_config)
