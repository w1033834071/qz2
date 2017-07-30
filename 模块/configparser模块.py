#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  configparser

parser = configparser.ConfigParser()

 # 将内容读取进内存
parser.read("ini", encoding="utf-8")
sections = parser.sections()
print(sections,type(sections))

r = parser.options("Edward")
print(r)