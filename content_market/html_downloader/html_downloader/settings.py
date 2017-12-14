# -*- coding: utf-8 -*-

BOT_NAME = 'html_downloader'

SPIDER_MODULES = ['html_downloader.spiders']
NEWSPIDER_MODULE = 'html_downloader.spiders'

CONCURRENT_REQUESTS = 32

# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# SPIDER_MIDDLEWARES = {
#    'html_downloader.middlewares.HtmlDownloaderSpiderMiddleware': 543,
# }

# DOWNLOADER_MIDDLEWARES = {
#    'html_downloader.middlewares.MyCustomDownloaderMiddleware': 543,
# }

ITEM_PIPELINES = {
    'html_downloader.pipelines.HtmlDownloaderPipeline': 300,
}

REDIS_URL = 'redis://localhost:6379/3'
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'

# if True user spop()
REDIS_START_URLS_AS_SET = True

# ============ Scheduler Settings ============
DETAIL_SCHEDULER_QUEUE_CLASS = 'hm_collections.queue.redis_queue.RedisSetQueue'
DETAIL_QUEUE_KEY = 'spider:parse:detail'
DETAIL_QUEUE_SERIALIZER = 'json'

CHAPTER_SCHEDULER_QUEUE_CLASS = 'hm_collections.queue.redis_queue.RedisSetQueue'
CHAPTER_QUEUE_KEY = 'spider:parse:chapter'
CHAPTER_QUEUE_SERIALIZER = 'json'

CONTENT_SCHEDULER_QUEUE_CLASS = 'hm_collections.queue.redis_queue.RedisSetQueue'
CONTENT_QUEUE_KEY = 'spider:parse:content'
CONTENT_QUEUE_SERIALIZER = 'json'
