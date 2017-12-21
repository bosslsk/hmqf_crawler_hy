# -*- coding: utf-8 -*-

import re
import json
import chardet

from scrapy import FormRequest
from scrapy_redis.spiders import RedisSpider
from html_downloader.items import HtmlDownloaderItem


class HtmlSpiderSpider(RedisSpider):
    name = "html_spider"
    redis_key = 'spider:html'
    reg_charset = re.compile(r"<meta .*?charset=\"?(.*?)\"?[\>;/ ]")
    handle_httpstatus_list = [400, 404]

    def make_request_from_data(self, data):
        data = json.loads(data)
        formdata = data.pop('formdata', None)
        headers = data.pop('headers', None)
        url = data['url']
        return FormRequest(
            url,
            meta={'data': data},
            headers=headers,
            formdata=formdata,
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response):
        charset = self.reg_charset.search(response.body)
        data = response.meta['data']
        item = HtmlDownloaderItem()
        item['url'] = data['url']
        item['url_type'] = data['url_type']
        item['config'] = data.pop('config', {})
        item['extra'] = data.pop('extra', {})
        if charset:
            item['html'] = response.body_as_unicode()
        else:
            item['html'] = response.body.decode(chardet.detect(response.body[:2000])['encoding'])
        yield item
