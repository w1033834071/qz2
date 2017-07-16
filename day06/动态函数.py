#!/usr/bin/env python
# -*- coding:utf-8 -*-

#动态函数
'''
(1122, 222, '11') <class 'tuple'>
{'k2': 456, 'k1': 123} <class 'dict'>
会自动分成元组和字典    厉害啦~~~~~~
*** 形参顺序不能换！！
'''

def f1(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

f1(1122,222,'11',k1 = 123,k2 = 456)
f1([11,22,33])