# -*- coding: utf-8 -*-
"""
create on 2017-11-24 下午3:47

author @heyao
"""

from content_market.parser.utils import Cleaner
from content_market.utils.log import get_logger


class BaseParser(object):
    def __init__(self, log_name=None, log_level="INFO", format_str=None, filename=None):
        log_name = log_name or __name__
        self.cleaner = Cleaner()
        self.logger = get_logger(log_name, log_level, format_str, filename)

    @classmethod
    def from_settings(cls, settings):
        log_level = settings.get("LOG_LEVEL", "INFO")
        format_str = settings.get("LOG_FORMAT", None)
        filename = settings.get("LOG_FILENAME", None)
        return cls(log_level, format_str, filename)

    @staticmethod
    def transform_word_count(word_count, site):
        if u'千' in site:
            return float(word_count) * 1000
        if u'万' in site:
            return float(word_count) * 10000
        if u'亿' in site:
            return float(word_count) * 100000000
        return float(word_count)

    def parse_source_list(self, content, url):
        raise NotImplementedError()

    def parse_detail(self, content, url):
        raise NotImplementedError()

    def parse_chapter_list(self, content, url):
        raise NotImplementedError()

    def parse_content(self, content, url=None):
        raise NotImplementedError()


if __name__ == '__main__':
    from content_market import config
    parser = BaseParser.from_settings(config)
    print parser.cleaner.clean("    awdadawdad ")
