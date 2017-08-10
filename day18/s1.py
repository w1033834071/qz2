#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,select

socket1 = socket.socket()
ip_port = ("127.0.0.1",8001)
socket1.bind(ip_port)
socket1.listen()

socket2 = socket.socket()
ip_port = ("127.0.0.1",8002)
socket2.bind(ip_port)
socket2.listen()

socket3 = socket.socket()
ip_port = ("127.0.0.1",8003)
socket3.bind(ip_port)
socket3.listen()

inputs = [socket1,socket2,socket3,]
while True:
    r_list,w_list,e_list = select.select(inputs,[],inputs,1)  # 监听句柄的变化
    for sk in r_list:
        sock,addr = sk.accept()
        sock.sendall(bytes("欢迎连接！",encoding='utf-8'))

    for sk in e_list:   # 监测到有错误后移除
        inputs.remove(sk)