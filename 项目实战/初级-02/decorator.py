#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 装饰器


def log(func):
    def wrapper(*args, **kvargs):
        '''
        :param args: 无名字的参数
        :param kvargs: 有名字的参数
        :return:
        '''
        print('before func', func.__name__)
        ret = func(*args, **kvargs)
        print('after func', func.__name__)
        return ret
    return wrapper

@log
def hello(name,age):
    print('hello ',name, age)

if __name__ == '__main__':
    hello('wanglinkai',20)