#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 只读  r
# f = open("ha.log",'r')
# data = f.read()
# f.close()
# print(data)

# 只写模式  w 不存在创建,存在清空
# f = open('ha1.log','w')
# f.write('456')
# f.close()

# 只写模式 x 不存在创建   存在报错！
# f = open('ha1.log','x')
# f.write('456')
# f.close()

# 追加模式  a 不存在创建   存在向后追加内容


# 只读模式   rb  以byte字节的方式读取   如果是  r  则读取时默认已经用utf-8的格式转换


# r+模式  先读后写  读后指针位置改变   写时指针直接跳到末尾
# f = open('ha.log','r+',encoding='utf-8')
# data = f.read()
# f.write('你好帅')
# print(data,f.tell())
# f.seek(0)
# d = f.read()
# print(d,f.tell())

# f.truncate() 是当前指针在什么位置   取指针及之前的文件数据   其他删除

# for line in f:    一行行读取文件数据   f.read()是一次性读完 如果数据过大  内存会撑不住
#     print(line)


# f.close() 可以不写
# with open('ha.log','r',encoding='utf-8') as f:
#     for line in f:
#         print(line)

#!!!!!!!! python2.7之后可以同时打开两个文件   牛！！！！！
with open('ha.log','r',encoding='utf-8') as f1, open('ha_copy.log','w',encoding='utf-8') as f2:
    for line in f1:
        f2.write(line)