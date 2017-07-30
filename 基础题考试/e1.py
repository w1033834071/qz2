#!/usr/bin/env python
# -*- coding:utf-8 -*-


def c():
    sum = 0
    for i in range(100,301):
        if i % 3 == 0 and i % 7 == 0:
            print(i)
            sum += i
    return sum

if __name__ == "__main__":
    ret = c()
    print(ret)