# -*- coding: utf-8 -*-
import socket
import time

def Client():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',8080))
    #time.sleep(2)
    print 'connect ok'
    print s.recv(1024)
    for data in ['zhao','wen']:
        s.send(data)
        print s.recv(1024)

    s.send('exit')
    s.close()

if __name__ == '__main__':
    Client()