#!/usr/bin/env python
# -*- coding -*-

li = [11,22,33,44,55,66,77,88,99]

dict = {'k1': [], 'k2':[]}
for i in li:
    if i < 66:
        dict['k1'].append(i)
    else:
        dict['k2'].append(i)
print(dict)

'''
作业二
1,移除空格
2,查找以 e开头的元素  并以c结尾的元素
'''

l1 = ['alex', '  eric', 'edward']
for i in l1:
    new_i = i.strip()
    if new_i.startswith('e') or new_i.startswith('A'):
        if new_i.endswith('c'):
            print(i)
