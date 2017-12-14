# -*- coding: utf-8 -*-
"""
create on 2017-11-24 上午11:42

author @heyao
"""


class Cleaner(object):
    def __init__(self):
        pass

    @staticmethod
    def clean(content):
        """清洗单段文本
        :param content: unicode. 段落文本 
        :return: unicode.
        """
        return content.replace(u'　', '').strip()

    def fit_transform(self, content, sep='\n', head='', end=''):
        """清洗篇章文本
        :param content: unicode. 段落文本。 
        :param sep: str. 段落间的分隔符. 默认 \n
        :param head: 清洗后的文本，需要添加的前缀，默认为 ''
        :param end: 清洗后的文本，需要添加的后缀，默认为 ''
        :return: unicode.
        """
        # TODO: add symbolDecode
        content = content.replace('<br>', '\n')
        return head + sep.join(self.clean(p) for p in content.split('\n') if self.clean(p)) + end
