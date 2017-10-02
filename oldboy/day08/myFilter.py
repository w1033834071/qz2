#!/usr/bin/env python
# -*- coding:utf-8 -*-

#模拟 filter()函数的运作过程


def myFilter(func,seq):
    result = []
    for i in seq:
        ret = func(i)
        if ret:
            result.append(i)
    return result

def fun(x):
    if x > 22:
        return True
    else:
        return False

r = myFilter(fun,[11,22,33,44])
print(r)