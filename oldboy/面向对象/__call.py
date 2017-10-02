#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo:

    def __init__(self):
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")
        return 0

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)


obj = Foo()  # 执行init
r = obj()   # 对象后面加括号执行__call__方法
print(r)

obj["k1"]  # => 对象后面加中括号会执行__getitem__方法
obj["k1"] = 123  # => 赋值会执行__setitem__方法

del obj["k1"]   # => 会执行__delitem__方法