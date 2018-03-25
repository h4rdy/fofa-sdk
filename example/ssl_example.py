# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time    : 2018/3/25
# @Author  : h4rdy <with.h4rdy@gmail.com>
# @File    : ssl_example.py

import pyfofa

email = 'with.h4rdy@gmail.com'
key = '123456'
search = pyfofa.FofaAPI(email, key)
for host, ip in search.get_data('cert="baidu.com"', 1, "host,ip")['results']:
    print(host, ip)
