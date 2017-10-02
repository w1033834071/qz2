#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

socket = socket.socket()
socket.bind(('127.0.0.1', 9999,))
socket.listen(5)
# 连接   客户端的地址信息
while True:
    sock, addr = socket.accept()
    sock.sendall(bytes("欢迎致电中国移动", encoding='utf-8'))
    while True:
        ret_bytes = sock.recv(1024)
        ret_str = str(ret_bytes, encoding='utf-8')
        print(ret_str)
        if ret_str == 'q':
            break
        sock.sendall(bytes(ret_str + '你好', encoding='utf-8'))
