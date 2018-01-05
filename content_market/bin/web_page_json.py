# -*- coding:utf-8 -*-
"""
    @author: harvey
    @time: 2018/1/3 18:35
    @subject: 生成测试文件(js接口加载章节列表)
"""

import os
import sys
import json

import requests
from content_market.parser.xxsy import Xxsy
from tests import base_dir

reload(sys)
sys.setdefaultencoding('utf-8')


def detail(parser, path, content):
    with open(os.path.join(path, 'book_detail.html'), 'w') as f:
        f.write(content)

    book_detail = parser.parse_detail(content, html_url)
    with open(os.path.join(path, 'book_detail.json'), 'w') as f:
        json.dump(dict(book_detail), f, ensure_ascii=False)


def chapter(parser, path, content):
    source_chapter = parser.parse_chapter_list(content, html_url)
    chapters = list(source_chapter)
    with open(os.path.join(path, 'chapters.json'), 'w') as f:
        json.dump([dict(c) for c in chapters], f, ensure_ascii=False)

    chapter_info = chapters[0]
    chapter = requests.get(chapter_info['url']).content
    with open(os.path.join(path, 'chapter_content.html'), 'w') as f:
        f.write(chapter)
    chapter_content = parser.parse_content(chapter, html_url)
    with open(os.path.join(path, 'chapter_content.txt'), 'w') as f:
        f.write(chapter_content)


def set_parameter(station, parser):
    path = os.path.join(base_dir, 'parser/data', station)
    if not os.path.isdir(path):
        os.makedirs(path)
    content_html = requests.get(html_url).content
    detail(parser, path, content_html)
    content_json = requests.get(json_url).content.decode('utf-8')
    chapter(parser, path, content_json)


if __name__ == '__main__':
    html_url = 'http://www.xxsy.net/info/897569.html'
    json_url = 'http://www.xxsy.net/partview/GetChapterList?bookid=897569&noNeedBuy=0&special=0'
    xxsy = Xxsy(__name__, "DEBUG")
    source = xxsy
    station = u'xxsy'
    set_parameter(station, source)
