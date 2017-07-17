#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 作用：
# 不改变原函数   在函数之前或之后再做点操作

# 装饰器原理
# 1、 将outer函数与需要的函数进行捆绑
# 2、 执行outer函数，并且将其下面的函数名、当做参数
# 3、 将outer的返回值重新赋值给f1 = outer的返回值
# 新f1函数 = inner

def outer(func):
    def inner():
        print("hello")
        print("hello")
        print("hello")
        r = func()
        print("end")
        print("end")
        print("end")
        return r
    return inner

#假设有核心代码 100个  不易做修改
def f1():
    print("f1")

def f2():
    print("f2")

def f3():
    print("f3")

def f4():
    print("f4")

@outer
def f100():
    print("f100")

f100()