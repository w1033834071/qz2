#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

socket = socket.socket()
address = ("127.0.0.1",8003)
socket.connect(address)

ret = str(socket.recv(1024),encoding='utf-8')
print(ret)