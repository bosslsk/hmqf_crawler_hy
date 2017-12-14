# -*- coding: utf-8 -*-
"""
create on 2017-12-13 下午2:36

author @heyao
"""

import re

reg = re.compile(r"\{(.*?)\}")


def find_keys(string):
    """find all keys in string with {key_name} format.
    :param string: str. 
    :return: list. 
    """
    if not (isinstance(string, str) or isinstance(string, unicode)):
        return []
    return reg.findall(string)


def inject(string, **url_info):
    keys = find_keys(string)
    if not keys:
        return string
    return string.format(**{k: url_info[k] for k in keys})
