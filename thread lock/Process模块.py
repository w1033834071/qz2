#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process
from threading import Thread

li = []

def foo(i):
    li.append(i)
    print("say hi", li)

if __name__ == "__main__":
    for i in range(10):       #将会创建十个进程  每个li都不共享内存
        p = Process(target=foo, args=(i,))
        p.start()

        t = Thread(target=foo, args=(i,))   #线程之间内存共享  li是一个
        t.start()
