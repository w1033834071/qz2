#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process

def f(name):
    print("hello", name)


if __name__ == '__main__':
    p = Process(target=f,args=('edward',))
    p.start()
    p.join()
