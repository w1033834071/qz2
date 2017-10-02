#!/usr/bin/env python
# -*- coding:utf-8 -*-

l1 = [11,22,33]
l2 = [22,33,44]

set_l1 = set(l1)
set_l2 = set(l2)

commons = set_l1.intersection(set_l2)
print(commons)