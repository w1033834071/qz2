#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

origin = "hello alex abcd 123"

r = re.split('a\w+',origin,maxsplit=1)
# 加个括号表示分组  所有结果 + 分组得到的结果
r1 = re.split('(a\w+)',origin,maxsplit=1)

print(r)
print(r1)

s = "1+1+(1*(1+2) + (2-1)) + 3+(1+(1+1))"
ret = re.split('\(([^()]+)\)',s)
print(ret)