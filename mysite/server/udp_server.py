# -*- coding: UTF-8 -*-
import socket
import requests
#socket通信客户端
def server():
    ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ser.bind(('127.0.0.1',49999))
    ser.listen(5)
    while 1:
        client,addr=ser.accept()
        print 'accept %s connect'%(addr,)
        data=client.recv(1024)
        print data
        client.send('get')
        client.close()

server()

class UDPServer(object):
    """docstring for UDPServer"""
    def __init__(self, arg):
        super(UDPServer, self).__init__()
        self.arg = arg

    def send_msg(self):
        pass

    def recv_msg(self):
        pass

    def close_connect(self):
        pass

    


