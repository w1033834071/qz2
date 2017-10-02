#!/usr/bin/env python
# -*- coding:utf-8 -*-



# 协程：   当遇到进行IO操作时自动切换任务  提高效率
from gevent import monkey; monkey.patch_all()

import gevent
from urllib import request

def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
    gevent.spawn(f, 'https://www.baidu.com/'),
    gevent.spawn(f, 'https://www.taobao.com/'),
    gevent.spawn(f, 'https://github.com/'),
])