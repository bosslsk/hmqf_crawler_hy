# -*- coding: utf-8 -*-
"""
create on 2017-12-06 下午12:02

author @heyao
"""

from scrapy import Item, Field


class BookSourceItem(Item):
    title = Field()
    author = Field()
    url = Field()
    book_id = Field()
    source = Field()
    published_at = Field()  # 新书上架时间
    category = Field()
    sub_category = Field()
    created_at = Field()
    updated_at = Field()
    folder_url = Field()
    status = Field()  # 连载状态
    introduction = Field()


class BookInfoItem(Item):
    title = Field()
    author = Field()
    url = Field()
    book_id = Field()
    source = Field()
    published_at = Field()
    category = Field()
    sub_category = Field()
    created_at = Field()
    updated_at = Field()
    folder_url = Field()
    status = Field()  # 书连载状态
    word_count = Field()  # 总字数
    introduction = Field()


class ChapterListItem(Item):
    title = Field()
    url = Field()
    chapter_ordinal = Field()
    chapter_id = Field()
    updated_at = Field()
    word_count = Field()
