#!/usr/bin/env python
# -*- coding:utf-8 -*-


#经典的冒泡排序算法
li = [55,44,2,1,4,44,-1]

for x in range(1,len(li)):
    for i in range(len(li) - x):
        if li[i] > li[i+1]:
            temp = li[i+1]
            li[i+1] = li[i]
            li[i] = temp

print(li)
