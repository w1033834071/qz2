#!/usr/bin/env python
# -*- coding -*-

#列出商品 选商品
# li = ['手机','电脑','鼠标垫','游艇']
# for i,j in enumerate(li):
#     print(i+1,j)
# num = int(input("num:"))
# if num > 0 and num <= len(li):
#     good = li[num-1]
#     print(good)
# else:
#     print('商品不存在')

dic = {
    "河北":{
        "石家庄":["鹿泉","真诚","元氏"],
        "邯郸":["永年","涉县","磁县"]
    },
    "河南":{
        "郑州":["1","2","3"],
        "开封":["4","5","6"]
    }
}

#循环输出所有的省
for p in dic:
    print(p)
str1 = input("请输入省份：")
for c in dic[str1]:
    print(c)
str2 = input("请输入城市：")
for d in dic[str1][str2]:
    print(d)

