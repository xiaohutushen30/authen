# -*- coding: UTF-8 -*-
import socket
#socket通信客户端
def server():
    ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ser.bind(('127.0.0.1',6789))
    ser.listen(5)
    while 1:
        client,addr=ser.accept()
        print 'accept %s connect'%(addr,)
        data=client.recv(1024)
        print data
        client.send('get')
        client.close()

server()