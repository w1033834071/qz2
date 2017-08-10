#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

#   服务端接收文件上传

socket = socket.socket()

ip_port = ("127.0.0.1",8888)
socket.bind(ip_port)
socket.listen(5)

while True:
    # 接收请求连接的客户端
    sock,addr = socket.accept()
    sock.sendall(bytes("连接成功！ 请开始上传数据", encoding='utf-8'))
    file_size = str(sock.recv(1024),encoding='utf-8')
    print("接收到文件大小：%s" % file_size)
    sock.sendall(bytes("开始传输",encoding='utf-8'))
    total_size = int(file_size)
    curr_size = 0  # 已接受文件大小
    f = open('copy.png','wb')
    while True:
        if curr_size == total_size:
            break
        data = sock.recv(1024)
        f.write(data)
        curr_size += len(data)
    print("传输完成！！！！")
    f.close()