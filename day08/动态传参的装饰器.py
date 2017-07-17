#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 动态传参的装饰器
# 传入动态参数且 内部已经自动能够识别传入的动态参数   牛！！！！
# 一个函数可以附加多个装饰器

'''
多装饰器原理：
    将outer的inner当作参数传递给了outer_0
    相当于outer_0中的func = inner(outer)
'''

def outer_0(func):
    def inner(*args,**kwargs):
        print("附加装饰器")
        ret = func(*args,**kwargs)
        return ret
    return inner

def outer(func):
    def inner(*args,**kwargs):
        print("hello")
        ret = func(*args,**kwargs)
        print("end")
        return ret
    return inner

@outer
def f1(a1):
    print("f1")
    return "f1返回值"

#一个函数可以附加多个装饰器
@outer_0
@outer
def f2(a1,a2):
    print("f2")
    return "f2返回值"

r = f2(1,1)
print(r)

@outer
def f3(a1,a2,a3):
    print("f3")
    return "f3返回值"

# r = f3(1,2,3)
# print(r)