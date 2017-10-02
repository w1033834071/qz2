#!/usr/bin/env python
# -*- coding:utf-8 -*-

s = " Edward 2222211"


#  其实返回的是一个元组或字典  并不是返回多个值
def c(string):
    blank_space = 0
    upper_case = 0
    lower_case = 0
    num = 0
    for i in s:
        if i.isspace():
            blank_space += 1
        elif i.islower():
            lower_case += 1
        elif i.isupper():
            upper_case += 1
        elif i.isnumeric():
            num += 1
    return blank_space,upper_case,lower_case,num



blank_space,upper_case,lower_case,num = c(s)
print(blank_space,upper_case,lower_case,num)