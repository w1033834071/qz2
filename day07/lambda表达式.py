#!/usr/bin/env python
# -*- coding:utf-8 -*-

def f1():
    return 123

# lambda表达式即为了代替一些点单的函数

f2 = lambda : 123

r1 =f1()
print(r1)
r2 = f2()
print(r2)


def f3(a1,a2):
    return a1 + a2

f4 = lambda a1,a2: a1 + a2

r3 = f3(1,1)
print(r3)
r4 = f4(1,1)
print(r4)