# -*- coding: utf-8 -*-
"""
create on 2017-12-19 下午4:29

author @heyao
"""

import sys

from os import makedirs
from os.path import join, isdir

reload(sys)
sys.setdefaultencoding('utf8')


def save_content(file_path, filename, content):
    if not isdir(file_path):
        makedirs(file_path)
    path = join(file_path, filename)
    with open(path, 'w') as f:
        f.write(content)
    return path
