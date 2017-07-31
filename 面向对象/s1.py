#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Oldboy:
    def fetch(self,backend):
        print(backend,self)



#   self 传递的就是 old_boy对象
old_boy = Oldboy()
old_boy2 = Oldboy()
print(old_boy,old_boy2)
old_boy.fetch("王林锴")