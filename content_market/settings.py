# -*- coding: utf-8 -*-
"""
create on 2017-12-12 下午6:02

author @heyao
"""


class Config(object):
    @classmethod
    def get(cls, attr_name, default=None):
        return getattr(cls, attr_name, default)


class DevelopmentConfig(Config):
    LOG_LEVEL = 'DEBUG'
    REDIS_URI = 'redis://localhost:6379/3'
    MONGO_URI = 'mongodb://localhost:27017'
    MONGO_DB_NAME = 'develop'
    MONGO_AUTH = {}


class ProductionConfig(Config):
    LOG_LEVEL = 'INFO'
    REDIS_URI = 'redis://localhost:6379/3'
    MONGO_URI = 'mongodb://localhost:27107'
    MONGO_DB_NAME = 'develop'
    MONGO_AUTH = {}


class TestConfig(Config):
    pass


config = dict(
    default=DevelopmentConfig,
    development=DevelopmentConfig,
    production=ProductionConfig,
    testing=TestConfig
)
