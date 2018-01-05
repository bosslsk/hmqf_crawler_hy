# -*- coding:utf-8 -*-
"""
    @author: harvey
    @time: 2018/1/3 18:35
    @subject: 生成测试文件
"""

import os
import sys
import json

import requests
from content_market.parser.lieshu import Lieshu
from content_market.parser.xxsy import Xxsy
from content_market.parser.biquge import Biquge
from content_market.parser.hongxiu import Hongxiu
from content_market.parser.shangshu import Shangshu
from tests import base_dir

reload(sys)
sys.setdefaultencoding('utf-8')


def product_file(parser, path, content):
    with open(os.path.join(path, 'book_detail.html'), 'w') as f:
        f.write(content)

    book_detail = parser.parse_detail(content, url)
    with open(os.path.join(path, 'book_detail.json'), 'w') as f:
        json.dump(dict(book_detail), f, ensure_ascii=False)

    source_chapter = parser.parse_chapter_list(content, url)
    chapters = list(source_chapter)
    with open(os.path.join(path, 'chapters.json'), 'w') as f:
        json.dump([dict(c) for c in chapters], f, ensure_ascii=False)

    chapter_info = chapters[0]
    # chapter = requests.get(chapter_info['url']).content.decode('gbk')
    chapter = requests.get(chapter_info['url']).content.decode('utf-8')
    with open(os.path.join(path, 'chapter_content.html'), 'w') as f:
        f.write(chapter)
    chapter_content = parser.parse_content(chapter, url)
    with open(os.path.join(path, 'chapter_content.txt'), 'w') as f:
        f.write(chapter_content)


def set_parameter(station, parser):
    path = os.path.join(base_dir, 'parser/data', station)
    if not os.path.isdir(path):
        os.makedirs(path)
    # content = requests.get(url).content.decode('gbk')
    content = requests.get(url).content.decode('utf-8')
    product_file(parser, path, content)


if __name__ == '__main__':
    # url = 'http://www.shangshu.cc/99/99390/'
    url = 'https://www.hongxiu.com/book/6972481904230701'
    # url = 'http://www.biquge5200.com/86_86306/'
    # url = 'http://www.lieshu.cc/2/2732/'
    shangshu = Shangshu(__name__, "DEBUG")
    hongxiu = Hongxiu(__name__, "DEBUG")
    biquge = Biquge(__name__, "DEBUG")
    xxsy = Xxsy(__name__, "DEBUG")
    lieshu = Lieshu(__name__, 'DEBUG')
    source = hongxiu
    station = u'hongxiu'
    set_parameter(station, source)
