#!/usr/bin/env python
# -*- coding:utf-8 -*-

#进制转换
#bin() 二进制

#oct() 八进制

# int() 十进制
#二进制转十进制
# r = int('1111',base = 2)
# print(r)

# hex() 十六进制

#bytes     字节
# bytearray 字节列表

#字节、字符串
# bytes('a',encoding='utf-8')


# chr()  数字转 ascill码对应的字符
# ord()  字符转对应的数字
#用法跳转至随机验证码

# eval() 函数   将字符串编程表达式
# exec() 函数   执行代码  没有返回值
# compile() 函数  编译代码  有返回值
# ret = eval("a + 3",{'a':97})
# print(ret)

# exec("for i in range(10):print(i)")


# filter(函数，可迭代对象)  过滤  每个元素经过函数后返回True则添加进ret   False则过滤掉
# def fun1(a):
#     return True
# ret = filter(fun1,[11,22])
# for i in ret:
#     print(i)

# ret = filter(lambda x: x > 11,[11,22])
# for i in ret:
#     print(i)



# map(函数，可迭代对象)   将对象所有元素迭代   经过函数后的新值存入ret
# def fun1(x):
#     if x % 2 == 1:
#         return x + 100
#     else:
#         return x
#
# ret = map(fun1,[1,2,3,4,5])
# ret = map(lambda x: x + 100 if x % 2 == 1 else x, [1,2,3,4,5])
# for i in ret:
#     print(i)


# iter()  创建一个可迭代的对象
# obj = iter([11,22,33])
# i = next(obj)
# print(i)
# yield() 生成器  暂未讲


# round() 四舍五入
# slice() 切片  相当于list中的内置方法   一般直接切片即可


#zip()   将两组可迭代的对象 变为键值对  第一组为键  对应  第二组的值

li1 = [1,2,3,4]
li2 = ['a','b','c','d']
ret = zip(li1,li2)
for i in ret:
    print(i)
