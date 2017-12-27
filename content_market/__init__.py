# -*- coding: utf-8 -*-
"""
create on 2017-11-24 上午11:39

author @heyao
"""

import os

from content_market.settings import config

config_name = os.environ.get("TOOLS_CONFIG_NAME", 'default')
config = config[config_name]
