#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Foo:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(self,"show")


#  反射  从类中直接操作成员或者  从对象中直接操作都可以！！  因为其内部有一个类对象指针 指向了该类
print(hasattr(Foo,"show"))

r = Foo("edward")
print(hasattr(r,"show"))