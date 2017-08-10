#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sock = socket.socket()
address = ("127.0.0.1",8001)
sock.connect(address)

while True:
    inp= input("内容：")
    sock.sendall(bytes(inp,encoding='utf-8'))
    ret = str(sock.recv(1024),encoding='utf-8')
    print(ret)
