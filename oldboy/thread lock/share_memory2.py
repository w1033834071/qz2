#!/usr/bin/env python
# -*- coding:utf-8 -*-

#共享数据的方式2

from multiprocessing import Process, Manager

def func(d,l):
    d[1] = 1
    d['2'] = 2
    d[0.25] = None
    l.reverse()

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = Process(target=func, args=(d,l))
        p.start()
        p.join()

        print(d)
        print(l)