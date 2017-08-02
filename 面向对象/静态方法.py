#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Provice:

    country = "中国"

    def __init__(self,name):
        self.name = name

    def show(self):
        print("show")

    @staticmethod    # 静态方法和对象没有关系
    def xo():
        print("xo")

    @classmethod
    def xxoo(cls):  #  比静态方法多了一个类参数
        print("xxoo")

    @property
    def end(self):  # 特性   将方法伪造成一个字段  调用不需要括号（不能传参）
        temp = "%s sb" %self.name
        return temp

    @end.setter    #  类似于JAVABean  给end方法设置值
    def end(self,value):
        self.name = value



# 通过类直接访问静态字段   静态方法  类方法
print(Provice.country)
Provice.xo()

# 通过对象去访问普通字段和方法
obj = Provice("河南")
obj.show()

Provice.xxoo()

r = obj.end
print(r)

# setter方法使用
obj.end = 123
print(obj.end)
