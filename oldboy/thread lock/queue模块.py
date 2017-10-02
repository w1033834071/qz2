#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import queue

q = queue.Queue(10)

def producer(i):
    print("producer:" + i)
    q.put(i)

def consumer():
    print(q.get())


for i in range(12):
    t = threading.Thread(target=producer, args=(i))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer)
    t.start()


