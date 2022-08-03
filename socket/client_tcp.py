#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
'''
https://docs.python.org/3/library/socket.html
'''

tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()# 'localhost'
port = 1234
addr = (host,port)
tcp_socket.connect(addr)

tcp_socket.send(str.encode("hello server","utf-8"))

full_msg = ''
while True:
    msg = tcp_socket.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8") # encode - перекодирует введенные данные в байты, decode - обратно
tcp_socket.close()

print(full_msg)

# Run:
# python socket/client_tcp.py