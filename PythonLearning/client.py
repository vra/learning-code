#!/usr/bin/env python

import socket

#configure requesting socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#HOST=localhost,PORT=8432,which must be same with server's listening port
s.connect(('127.0.0.1',8432))

#send message to server
s.sendall('Can you hear me?')
#get message from server
reply=s.recv(1024)

print 'reply from server  is :',reply
s.close()
