# -*- coding:utf-8 -*-
"""
    @author: harvey
    @time: 2017/12/19 16:28
    @subject: 
"""
import requests
import urlparse
from urlparse import urljoin

import sys
from urlparse import urljoin

from lxml import etree

from content_market.parser.base_parser import BaseParser
from content_market.parser.items import BookInfoItem, ChapterListItem

reload(sys)
sys.setdefaultencoding('utf-8')


class Shangshu(BaseParser):
    def __init__(self, log_name=None, log_level="INFO", format_str=None, filename=None):
        super(Shangshu, self).__init__(log_name, log_level, format_str, filename)

    def parse_detail(self, content, url):
        self.logger.debug('Received info')
        item = BookInfoItem()
        if u'出现错误' in content:
            return item
        sel = etree.HTML(content)
        item['folder_url'] = urljoin(url, sel.xpath('//img[@class="BookImg"]/@src')[0])
        item['title'] = sel.xpath('//img[@class="BookImg"]/@alt')[0]
        item['url'] = url
        item['author'] = sel.xpath('//h2[@class="BookAuthor"]/a/text()')[0]
        item['category'] = sel.xpath('//h2[@class="BookAuthor"]/text()')[1].strip().split(u'：')[-1]
        item['sub_category'] = ''
        item['word_count'] = 0
        book_id = self.get_book_id(item['url'])
        item['status'] = self.parse_status(book_id)
        item['introduction'] = sel.xpath('//h3[@class="BookIntro"]/text()')[0].replace(' ', '').strip()[3:]
        # item['status'] = sel.xpath('//span[@id="adbanner_1"]/text()')[0][:3]
        item['introduction'] = self.cleaner.fit_transform('\n'.join(sel.xpath('//h3[@class="BookIntro"]/text()')))
        return item

    def get_book_id(self, url):
        url_path = urlparse.urlparse(url).path
        book_id = url_path.split('/')[2]
        return book_id

    def parse_status(self, book_id):
        response = requests.get('http://www.shangshu.cc/modules/article/articleinfo.php?id={}'.format(book_id))
        status = response.content.decode('gbk').split('"')[1][:3]
        return status

    def parse_source_list(self, content, url):
        pass

    def parse_chapter_list(self, content, url):
        try:
            sel = etree.HTML(content)
        except ValueError:
            raise ValueError("can't parse any volume")
        chapters = sel.xpath('//ul[@class="ListRow"]/li/a')[:-2]
        chapter_ordinal = 1
        for chapter in chapters:
            try:
                item = ChapterListItem()
                item['url'] = urljoin(url, chapter.xpath('./@href')[0])
                item['title'] = chapter.xpath('./text()')[0]
                item['updated_at'] = None
                item['word_count'] = 0
                item['chapter_ordinal'] = chapter_ordinal
                chapter_ordinal += 1
                yield item
            except Exception as e:
                self.logger.error(e)

    def parse_content(self, content, url=None):
        sel = etree.HTML(content)
        return self.cleaner.fit_transform('\n'.join(sel.xpath('//div[@id="content"]/text()')))
