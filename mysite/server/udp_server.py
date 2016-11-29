#coding=utf-8

import socket
import time
import threading
import requests

class UdpServer(object):
    """docstring for UdpServer"""
    api_url = "http://127.0.0.1:8000/authen/api/cr_status/"
    def __init__(self):
        super(UdpServer, self).__init__()
        self.host = "localhost"
        self.buffsize = 1024
        self.port = 49999
        self.addr = (self.host, self.port)
        self.UDPSerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
        self.UDPSerSocket.bind(self.addr)

    def run_server(self):
        while True:
            try:
                self.UDPSerSocket.settimeout(0.5)
                data,addr = self.UDPSerSocket.recvfrom(self.buffsize)
                threading.Thread(target=self.receive,args=(data,addr)).start()
                if self.UDPSerSocket is None:
                    break
            except socket.timeout:
                continue
            

    def receive(self,data, addr):
        print 'Received',data,'from',addr,'in [%s]'%time.ctime()
        protocol_header = data[0:4]
        if protocol_header != "464B":
            msg = "protocol header error"
            self.UDPSerSocket.sendto('[%s]:%s'%(time.ctime(),msg),addr)
            return
        date_style = data[4:6]
        if date_style == "01":
            self.process_time(addr,data)
        elif date_style == "03":
            self.process_data(addr,data)
        else:
            msg = "data style error"
            self.UDPSerSocket.sendto('[%s]:%s'%(time.ctime(),msg),addr)
            return

    def process_time(self,addr,data):
        sn = data[8:17]
        date_str = time.strftime("%Y %m %d %H %M %S %w",time.localtime())
        date_list = date_str.split(" ")
        year = int(date_list[0]) - 2000
        month = int(date_list[1])
        day = int(date_list[2])
        hour = int(date_list[3])
        minute = int(date_list[4])
        second = int(date_list[5])
        week = int(date_list[6])

        msg = "464B" + "02" + "xx" + sn + hex(year)[2:].upper() + hex(month)[2:].upper() + hex(day)[2:].upper() + \
        hex(week)[2:].upper() + hex(hour)[2:].upper() + hex(minute)[2:].upper() + hex(second)[2:].upper()
        lenth = len(msg)
        msg = msg.replace("xx",hex(lenth)[2:].upper())  
        self.UDPSerSocket.sendto('%s' % msg,addr)
        return

    def process_data(self,addr,data):
        sn = data[8:24]
        person_num = int(data[24:26],16)
        person_info = data[26:50]
        status = int(data[50:52],16)
        year = int(data[52:54],16) + 2000
        month = int(data[54:56],16)
        day = int(data[56:58],16)
        week = int(data[58:60],16)
        hour = int(data[60:62],16)
        minute = int(data[62:64],16)
        second = int(data[64:66])
        date = "%s-%s-%s %s:%s:%s" % (year,month,day,hour,minute,second)
        http_data = {
            "sn":sn,
            "person_num":person_num,
            "person_info":person_info,
            "status":status,
            "date":date,
        }
        re = requests.post(url=self.api_url, data=http_data)
        if re.status_code == 200:
            self.UDPSerSocket.sendto(re.text,addr)
        else:
            self.UDPSerSocket.sendto(str(re.status_code),addr)
    def close_server(self):
        self.UDPSerSocket.close()
        self.UDPSerSocket = None


if __name__ == '__main__':
    udp_sr = UdpServer()
    udp_sr.run_server()










