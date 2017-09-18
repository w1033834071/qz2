#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading,time

globals_num = 0

lock = threading.RLock()

def func():
    lock.acquire()   #获得锁

    global globals_num

    globals_num += 1
    time.sleep(1)
    print(globals_num)

    lock.release()   #释放锁


for i in range(10):
    t = threading.Thread(target= func)
    t.start()



