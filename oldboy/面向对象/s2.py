#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Oldboy:
    def fetch(self):
        print(self.backend)

    def add(self,record):
        print(record)


old_boy = Oldboy()
# 在对象中封装变量
old_boy.backend = "www.linkwang.com"   #  如果该变量使用频繁   可以这样创建
old_boy.fetch()

old_boy2 = Oldboy()
old_boy2.backend = "www.linkwang2.com"
old_boy2.fetch()

# 封装