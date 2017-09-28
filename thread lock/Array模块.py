#!/usr/bin/env python
# -*- coding:utf-8 -*-


from multiprocessing import Process,Array

temp = Array('i',[11,22,33,44])

def Foo(i):
    temp[i] = 100 + i
    for item in temp:
        print(item)

if __name__ == "__main__":
    for i in range(2):
        p = Process(target=Foo, args=(i,))
        p.start()

# for item in temp:
#     print(item)