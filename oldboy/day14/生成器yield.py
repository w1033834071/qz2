#!/usr/bin/env python
# -*- coding:utf-8 -*-

# def xrange():
#     print("11")
#     yield 1
#
#     print("22")
#     yield 2
#
#     print("33")
#     yield 3
#
#
# r = xrange()
# ret = r.__next__()
# print(ret)
#
# ret = r.__next__()
# print(ret)
#
# ret = r.__next__()
# print(ret)


def xrange(n):
    '''
    模拟xrange()的执行过程
    :param n:
    :return:
    '''
    start = 0
    while True:
        if start > n:
            return
        yield start
        start += 1

# r叫做生成器，仅具有生成能力
r = xrange(10)
n1 = r.__next__()
n2 = r.__next__()
n3 = r.__next__()
n4 = r.__next__()
n5 = r.__next__()
n6 = r.__next__()
n7 = r.__next__()
n8 = r.__next__()
n9 = r.__next__()
n10 = r.__next__()
print(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10)