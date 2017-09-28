#!/usr/bin/env python
# -*- coding:utf-8 -*-

import queue
import threading
import time

class ThreadPool(object):  # 自定义的low版线程池

    def __init__(self,max_num = 20):
        self.queue = queue.Queue(max_num)
        for i in range(max_num):
            self.queue.put(threading.Thread)


    def get_thread(self):
        return self.queue.get()

    def add_thread(self):
        self.queue.put(threading.Thread)


def func(pool,i):
    time.sleep(1)
    print(i)
    pool.add_thread()

if __name__ == '__main__':

    pool = ThreadPool(10)

    for i in range(100):
        thread = pool.get_thread()
        t = thread(target=func, args=(pool,i,))
        t.start()
