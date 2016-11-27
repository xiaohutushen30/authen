# -*- coding: UTF-8 -*-
import socket
#socket通信客户端
def client():
    mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysocket.connect(('127.0.0.1',6789))
    mysocket.send('hello')
    while 1:
        data=mysocket.recv(1024)
        if data:
           print data
        else:
            break
    mysocket.close()
client()