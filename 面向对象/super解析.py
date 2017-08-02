#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Animal:
    def __init__(self):
        print("A 构造方法 ")
        self.A = "动物"

class Cat(Animal):
    def __init__(self):
        print("B 构造方法 ")
        self.B = "猫"
        super(Cat,self).__init__()    # self 在本例中是c对象  super的执行顺序和继承相同

c = Cat()
print(c.__dict__)
