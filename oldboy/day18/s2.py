#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,select

socket = socket.socket()
ip_port = ("127.0.0.1",8001)
socket.bind(ip_port)
socket.listen()

inputs = [socket,]
outputs = []  # 保存接收到信息的对象
msg_dict = {} # 消息字典

while True:
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)  # 监听句柄的变化
    for sk_or_conn in r_list:
        if sk_or_conn == socket:            # 有新连接
            sock,addr = sk_or_conn.accept()
            inputs.append(sock)
            msg_dict[sock] = []
        else:
            # 老用户发消息
            try:
                data_bytes = sk_or_conn.recv(1024)
            except Exception as e:
                inputs.remove(sk_or_conn)
            else:
                # 接收到正常消息
                data_str = str(data_bytes,encoding='utf-8')
                msg_dict[sk_or_conn].append(data_str)
                outputs.append(sk_or_conn)

    for conn in w_list:
        msg_str = msg_dict[conn][0]
        del msg_dict[conn][0]
        conn.sendall(bytes(msg_str + "好",encoding='utf-8'))
        outputs.remove(conn)