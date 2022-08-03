#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
'''
https://docs.python.org/3/library/socket.html
'''

#первый параметр socket_family может быть AF_INET или AF_UNIX
#второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()# 'localhost'
port = 1234
addr = (host,port)

tcp_socket.bind(addr)#bind - связывает адрес и порт с сокетом
tcp_socket.listen(5)#listen - запускает прием TCP

while True:
    #Если мы захотели выйти из программы
    question = input('Do you want to quit? y\\n: ')
    if question == 'y': break
    
    #accept - принимает запрос и устанавливает соединение, (по умолчанию работает в блокирующем режиме)
    #устанавливает новый сокет соединения в переменную conn и адрес клиента в переменную addr
    conn,addr = tcp_socket.accept()
    print(f"Connection from {addr} has been established!")
    
    data = conn.recv(1024) #recv - получает сообщение TCP
    if data != None:
        print(data)
    
    conn.send(bytes("Welcom to the server!","utf-8"))#send - передает сообщение TCP
    conn.close()#close - закрывает сокет
    
tcp_socket.close()    

# Run:
# python socket/server_tcp.py 
    