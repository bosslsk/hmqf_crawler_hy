# -*- coding: utf-8 -*-
"""
create on 2017-11-27 上午11:15

author @heyao
"""

import json

from nose.tools import assert_list_equal, assert_is_instance, assert_dict_equal, assert_equal

from content_market.parser.shangshu import Shangshu


class TestShangshu(object):
    def setUp(self):
        self.shangshu = Shangshu()

    def tear_down(self):
        pass

    def test_chapter_list(self):
        with open('parser/data/shangshu/book_detail.html', 'r') as f:
            content = f.read().decode('utf-8')
        with open('parser/data/shangshu/chapters.json', 'r') as f:
            real_chapters = json.load(f)
        url = 'http://www.shangshu.cc'
        chapters = self.shangshu.parse_chapter_list(content, url)
        assert_is_instance(chapters, type((i for i in (1,))))
        assert_list_equal(list(chapters), real_chapters)

    def test_chapter_content(self):
        with open('parser/data/shangshu/chapter_content.html', 'r') as f:
            content_page = f.read().decode('utf-8')
        with open('parser/data/shangshu/chapter_content.txt', 'r') as f:
            content = f.read().decode('utf-8')
        assert_equal(content, self.shangshu.parse_content(content_page))

    def test_book_detail(self):
        with open('parser/data/shangshu/book_detail.html', 'r') as f:
            content = f.read().decode('utf-8')
        with open('parser/data/shangshu/book_detail.json', 'r') as f:
            book_detail = json.load(f)
        url = 'http://www.shangshu.cc/99/99390/'
        info = self.shangshu.parse_detail(content, url)
        assert_dict_equal(book_detail, dict(info))
