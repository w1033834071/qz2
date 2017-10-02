#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 客户端


import socket

s = socket.socket()
s.connect(("127.0.0.1", 9999))
ret = str(s.recv(1024), encoding='utf-8')
print(ret)
while True:
    inp = input("内容：")
    if inp == 'q':
        s.sendall(bytes(inp, encoding='utf-8'))
        break
    else:
        s.sendall(bytes(inp, encoding='utf-8'))
        ret_str = str(s.recv(1024), encoding='utf-8')
        print(ret_str)

s.close()
