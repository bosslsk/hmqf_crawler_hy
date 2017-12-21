# -*- coding: utf-8 -*-
"""
create on 2017-12-14 上午10:16

author @heyao
"""

from scrapy.utils.misc import load_object


class Scheduler(object):
    def __init__(self, redis_server, key, queue_cls, queue_serializer=None, dont_serial=False):
        """scheduler 
        :param redis_server: `redis.Redis` object 
        :param key: str. queue key
        :param queue_cls: str, full path of queue class 
        :param queue_serializer: None or str, if is None, then it will use `pickle`
        :param dont_serial: bool. if True, queue_serializer will not be used
        """

        def import_object(obj):
            try:
                obj = __import__(obj)
            except ImportError:
                obj = load_object(obj)
            return obj

        queue_cls = load_object(queue_cls) if isinstance(queue_cls, str) else queue_cls
        queue_serializer = import_object(queue_serializer) if isinstance(queue_serializer, str) else queue_serializer
        self.redis_server = redis_server
        self.queue_cls = queue_cls
        self.queue = queue_cls(redis_server, key, queue_serializer, dont_serial)

    def __len__(self):
        return len(self.queue)

    @classmethod
    def from_settings(cls, redis_server, settings, prefix=""):
        if prefix:
            prefix = prefix + '_'
        queue_cls_str = settings.get(prefix + "SCHEDULER_QUEUE_CLASS")
        queue_cls = load_object(queue_cls_str)
        queue_key = settings.get(prefix + "QUEUE_KEY")
        queue_serializer = settings.get(prefix + "QUEUE_SERIALIZER", None)
        if queue_serializer:
            try:
                queue_serializer = __import__(queue_serializer)
            except ImportError:
                queue_serializer = load_object(queue_serializer)
        dont_serial = settings.get("DONT_SERIAL", False)
        return cls(redis_server, queue_key, queue_cls, queue_serializer, dont_serial)

    def schedul(self, data):
        self.queue.push(data)
        return True

    def has_pending_requests(self):
        return len(self)
