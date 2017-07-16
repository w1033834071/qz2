#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

temp = ""
for i in range(6):
    num = random.randrange(start=0,stop=4)
    if num == 1 or num == 3:
        rad1 = random.randrange(0,10)
        temp += str(rad1)
    else:
        rad2 = random.randrange(65,91)
        c2 = chr(rad2)
        temp += c2

print(temp)

