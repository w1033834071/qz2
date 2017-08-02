#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
class A:
    def bar(self):
        print("bar")
        self.f1()    #  self 是调用者对象   所以此种情况self会找到C中的f1()


class B(A):
    def f1(self):
        print("B")

class C:
    def f1(self):
        print("C")


class D(C,B):
    pass

d1 = D()
d1.f1()
d1.bar()
