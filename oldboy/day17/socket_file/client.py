#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,os

#  客户端

socket = socket.socket()
server_address = ("127.0.0.1",8888)
socket.connect(server_address)
ret = str(socket.recv(1024), encoding='utf-8')
print(ret)

file_size = os.stat('1.jpg').st_size
socket.sendall(bytes(str(file_size),encoding='utf-8'))
ret = socket.recv(1024)
if str(ret,encoding='utf-8') == '开始传输':

    with open('1.jpg','rb') as f:
        for line in f:
            socket.sendall(line)
            # print("开始传输 %s %%" % (int(line)/int(file_size))*100)
print("传输完成")
socket.close()

# while True:

