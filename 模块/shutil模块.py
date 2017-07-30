#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shutil


# file1 = open("ini","r",encoding="utf-8")
# print(file1,type(file1))
# 将文件内容拷贝到另一个文件中
# shutil.copyfileobj(open("ini","r",encoding="utf-8"),open("ini_copy","w",encoding="utf-8"))


import zipfile

# 压缩
# z = zipfile.ZipFile("压缩.zip", "w")
# z.write("ini")
# z.write("ini_copy")
# z.close()

# 解压缩

z = zipfile.ZipFile("压缩.zip",'r')
z.extractall()
z.close()



