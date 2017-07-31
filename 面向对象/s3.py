#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Person:

    def __init__(self,name,age,weight):
        self.Name = name
        self.Age = age
        self.Weight = weight

    def jianshen(self):
        '''
        健身  体重 -1
        :return:
        '''
        self.Weight -= 1

    def chi(self):
        '''
        吃  体重 + 2
        :return:
        '''
        self.Weight += 2

linkwang = Person("linkwang",20,110)
linkwang.chi()
print("王林锴吃后的体重：%s" % linkwang.Weight)
linkwang.jianshen()
linkwang.jianshen()
linkwang.jianshen()
print("王林锴健身后的体重：%s" % linkwang.Weight)
