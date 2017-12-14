# -*- coding: utf-8 -*-
"""
create on 2017-12-12 下午7:00

author @heyao
"""

import redis
import pymongo

from content_market import config

redis_connection_pool = redis.ConnectionPool.from_url(config.get("REDIS_URI"))
client = pymongo.MongoClient(config.get("MONGO_URI"))
mongo = client[config.get("MONGO_DB_NAME")]
auth = config.get("MONGO_AUTH")
if auth:
    mongo.authenticate(**auth)
