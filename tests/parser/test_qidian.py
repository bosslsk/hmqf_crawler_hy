# -*- coding: utf-8 -*-
"""
create on 2017-11-27 上午11:15

author @heyao
"""

import json

from nose.tools import assert_list_equal, assert_is_instance, assert_dict_equal, assert_equal

from content_market.parser.qidian import Qidian


class TestQidian(object):
    def setUp(self):
        self.qidian = Qidian()

    def tear_down(self):
        pass

    def test_source_list(self):
        with open('parser/data/qidian/source_list.html', 'r') as f:
            content = f.read().decode('utf-8')
        with open('parser/data/qidian/source_list.json', 'r') as f:
            result = json.load(f)
        url = 'https://www.qidian.com'
        source_list = self.qidian.parse_source_list(content, url)
        assert_list_equal(list(source_list), result)

    def test_chapter_list(self):
        with open('parser/data/qidian/book_detail.html', 'r') as f:
            content = f.read().decode('utf-8')
        with open('parser/data/qidian/chapters.json', 'r') as f:
            real_chapters = json.load(f)
        url = 'https://book.qidian.com'
        chapters = self.qidian.parse_chapter_list(content, url)
        assert_is_instance(chapters, type((i for i in (1,))))
        assert_list_equal(list(chapters), real_chapters)

    def test_chapter_content(self):
        with open('parser/data/qidian/chapter_page.html', 'r') as f:
            content_page = f.read().decode('utf-8')
        with open('parser/data/qidian/chapter_content.html', 'r') as f:
            content = f.read().decode('utf-8')
        assert_equal(content, self.qidian.parse_content(content_page))

    def test_book_detail(self):
        with open('parser/data/qidian/book_detail.html', 'r') as f:
            content = f.read().decode('utf-8')
        with open('parser/data/qidian/book_detail.json', 'r') as f:
            book_detail = json.load(f)
        url = 'https://book.qidian.com/info/1010696129'
        info = self.qidian.parse_detail(content, url)
        assert_dict_equal(book_detail, dict(info))
