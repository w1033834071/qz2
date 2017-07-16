#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# def f1(a1,a2):
#     if a1 > 10000:
#         return
#     print(a1,a1/a2)
#
#     a3 = a1 + a2
#     f1(a2,a3)
#
# f1(1,1)


#用递归写出斐波那契数列的第十个数
def fibo(depth, a1, a2):
    if depth == 10:
        return a1
    a3 = a1 + a2
    r = fibo(depth+1, a2, a3)
    return r

ret = fibo(1, 1, 1)
print(ret)