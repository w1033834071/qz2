#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 当函数作为参数传递时  函数加（）就是执行函数   不加括号就是当做变量
def fun1(arg):
    print(arg)

def x():
    print("I'm X")

print(x)
fun1(x)