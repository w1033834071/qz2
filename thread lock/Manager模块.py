#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process,Manager


 # 进程间的数据共享


def Foo(i,dic):
    dic[i] = 100 + i
    print(len(dic))

if __name__ == "__main__":
    manager = Manager()
    dic = manager.dict()

    for i in range(2):
        p = Process(target=Foo, args=(i,dic))
        p.start()
        p.join()