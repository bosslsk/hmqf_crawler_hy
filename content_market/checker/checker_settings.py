# -*- coding: utf-8 -*-
"""
create on 2017-12-13 上午9:57

author @heyao
"""

hosts_config = [
    {
        'name': 'QIDIAN_DETAIL_HTML',
        'host': 'book.qidian.com',
        'path': r'/info/[0-9].*?',
        'queries': None,
        'data_url': '{url}',
        'formdata': None,
        'headers': None,
        'status': 1,
        'parser': 'Qidian',
        'parse_func': 'parse_detail'
    },
    {
        'name': 'QIDIAN_DETAIL_JSON',
        'host': 'book.qidian.com',
        'path': r'/ajax/book/category',
        'queries': None,
        'data_url': '{url}',
        'formdata': None,
        'headers': {'Cookie': '_csrfToken={csrf_token}'},
        'status': 0,
        'parser': 'QidianJson',
        'parse_func': 'parse_detail'
    },
    {
        'name': 'JJWX_DETAIL_JSON',
        'host': 'www.jjwxc.net',
        'path': '/onebook.phchapter_request_datap',
        'queries': None,
        'data_url': 'http://android.jjwxc.net/androidapi/novelbasicinfo?novelId={book_id}',
        'formdata': None,
        'headers': None,
        'status': 1,
        'parser': 'JinJiang',
        'parse_func': 'parse_detail'
    },
    {
        'name': 'SHANGSHU_DETAIL_HTML',
        'host': 'www.shangshu.cc',
        'path': r'/[0-9]*.?/[0-9]*.?/',
        'queries': None,
        'data_url': '{url}',
        'formdata': None,
        'headers': None,
        'status': 1,
        'parser': 'Shangshu',
        'parse_func': 'parse_detail'
    }
]

chapter_config = [
    {
        'host': 'book.qidian.com',
        'path': r'/info/[0-9].*?',
        'data_url': '{url}',
        'formdata': None,
        'headers': None,
        'status': 1,
        'parser': 'Qidian',
        'parse_func': 'parse_chapter_list',
        'content_config': {
            'data_url': '{url}',
            'formdata': None,
            'headers': None,
            'parser': 'Qidian',
            'parse_func': 'parse_content'
        }
    },
    {
        'host': 'www.jjwxc.net',
        'path': '/onebook.php',
        'data_url': 'http://app-cdn.jjwxc.net/androidapi/chapterList?novelId={book_id}',
        'formdata': None,
        'headers': None,
        'status': 1,
        'parser': 'JinJiang',
        'parse_func': 'parse_chapter_list',
        'content_config': {
            'data_url': 'http://android.jjwxc.net/androidapi/chapterContent',
            'formdata': {'chapterId': '{chapter_id}', 'novelId': '{book_id}', 'versionCode': '0'},
            'headers': None,
            'parser': 'JinJiang',
            'parse_func': 'parse_content'
        }
    },
    {
        'host': 'www.shangshu.cc',
        'path': r'/[0-9]*.?/[0-9]*.?/',
        'data_url': '{url}',
        'formdata': None,
        'headers': None,
        'status': 1,
        'parser': 'Shangshu',
        'parse_func': 'parse_chapter_list',
        'content_config': {
            'data_url': '{url}',
            'formdata': None,
            'headers': None,
            'parser': 'Shangshu',
            'parse_func': 'parse_content'
        }
    }
]
