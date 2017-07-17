#!/usr/bin/env python
# -*- coding:utf-8 -*-

def outer(func):
    def inner(a1,a2):
        print("hello")
        ret = func(a1,a2)
        print("end")
        return ret
    return inner

@outer
def f1(a1,a2):
    print("非常复杂的逻辑")
    return a1 + a2



r = f1(1,1)
print(r)