# -*- coding:utf-8 -*-
"""
    @author: harvey
    @time: 2018/1/8 10:49
    @subject: 新增存储方式：json格式
"""
import os


def save_json(lines):
    result = '<p>' + '</p>\n<p>'.join(line.strip() for line in lines) + '</p>'
    print result


if __name__ == '__main__':
    with open(r'H:\HM\Spider_book\896809\1.txt', 'r') as f:
        lines = [line for line in f]
        save_json(lines)
