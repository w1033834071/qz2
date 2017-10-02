#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 全局变量默认都大写

PERSON = 'alex'

def fun1():
    a = 123
#若要修改全局变量PERSON   没有global默认创建的是局部变量PERSON
    global PERSON
    PERSON = 'eric'

    print(PERSON)


fun1()