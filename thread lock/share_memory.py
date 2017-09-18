#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 共享数据的方式1
from multiprocessing import Process, Value, Array

def func(n,a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)

    arr = Array('i', range(10))

    p1 = Process(target=func, args=(num,arr))
    p2 = Process(target=func, args=(num,arr))  #反转后再反转

    p1.start()
    p2.start()
    p1.join()
    p2.join()


    print(num.value)
    print(arr[:])
