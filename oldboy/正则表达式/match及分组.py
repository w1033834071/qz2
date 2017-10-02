#!/usr/bin/env python
# -*- coding:utf-8 -*-


import re

origin = "hello edward aaaaaaa 19"

# r = re.match("h\w+",origin)
# r = re.match("(h)(\w+)",origin)
r = re.match("(?P<n1>h)(?P<n2>\w+)",origin)

print(r.group())  # 获取匹配到的所有结果
print(r.groups()) # 获取模型中匹配到的分组结果
print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组


ret = re.search("e(\w+).*(?P<name>\d)$",origin)
print(ret.group())
print(ret.groups())
print(ret.groupdict())