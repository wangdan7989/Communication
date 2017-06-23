# -*- coding: utf-8 -*-
import socket
import time
from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='hello',command = self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message','hello,%s'% name)


def Client(data):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1',8080))
    #time.sleep(2)
    print 'connect ok'
    print s.recv(1024)
    #for da in data:
    s.send(data)
    print s.recv(1024)

    s.send('exit')
    s.close()

if __name__ == '__main__':
    #data = raw_input("please input your data:")
    #print "data:",data
    #Client(data)
    app = Application()
    app.master.title('hello world')
    app.mainloop()