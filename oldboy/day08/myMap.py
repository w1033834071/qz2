#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 自定义map() 函数
def myMap(func,seq):
    result = []
    for i in seq:
        ret = func(i)
        result.append(ret)
    return result

def fun(x):
    return x + 1

r = myMap(fun,[11,22,33,44])
print(r)