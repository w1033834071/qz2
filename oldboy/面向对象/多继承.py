#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 多继承
# 优先自己、左边、右边  （同级）
class Dad:
    def piao(self):
        print("Dad 嫖")

    def du(self):
        print("Dad 赌")


class Uncle:
    def piao(self):
        print("Uncle 嫖")

    def du(self):
        print("Uncle 赌")

    def kanshu(self):
        print("Uncle 看书")

class Son(Dad,Uncle):
    def chi(self):
        print("son 吃！")

    def he(self):
        print("son 喝")

son = Son()
son.piao()
son.kanshu()

