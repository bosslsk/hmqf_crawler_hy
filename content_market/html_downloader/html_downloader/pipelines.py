# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
from scrapy.conf import settings
from scheduler import Scheduler


class HtmlDownloaderPipeline(object):
    def open_spider(self, spider):
        redis_uri = settings.get("REDIS_URL")
        r = redis.StrictRedis.from_url(redis_uri)
        self.detail_scheduler = Scheduler.from_settings(r, settings, prefix='DETAIL')
        self.chapter_scheduler = Scheduler.from_settings(r, settings, prefix='CHAPTER')
        self.content_scheduler = Scheduler.from_settings(r, settings, prefix='CONTENT')

    def process_item(self, item, spider):
        if item['url_type'] == 'detail':
            self.detail_scheduler.schedul(dict(item))
        elif item['url_type'] == 'chapter':
            self.chapter_scheduler.schedul(dict(item))
        elif item['url_type'] == 'content':
            self.content_scheduler.schedul(dict(item))
        return item

    def close_spider(self, spider):
        pass
