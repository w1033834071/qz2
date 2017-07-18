#!/usr/bin/env python
# -*- coding:utf-8 -*


import re

#正则表达式

# 1，元字符
#  . 表示除换行符外的任意字符都可匹配
#  ^ 表示开头是否以xxx开头
# r = re.findall('^alex','alex is SB')
# print(r)

# $ 表示是否以xxx结尾
# r = re.findall('alex$','hello alex')
# print(r)

# * + ? { } 处理‘重复’的字符
# ‘*’ 表示‘x’出现0次或多次  此处为‘贪婪匹配’
# r = re.findall('alex*','alexxxxxxxx')
# print(r)

# ‘+’表示出现一次或多次
# ‘？’表示出现0次或1次
# {3,5}表示匹配3-5次都可以
# [bc] 表示匹配到b或c  'bc'不能同时出现
# [^1-9] 表示匹配‘非’1-9的其他字符

# p = re.compile(r'\d+')
# li = p.split('one1two2three3four4')
# print(li)
# 结果 ['one', 'two', 'three', 'four', '']

ret = re.split('[bc]','abcd')
print(ret)




