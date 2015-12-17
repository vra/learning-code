#!/usr/bin/env python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#bind((Host,Port))
s.bind(('',8432))

#socket wait
s.listen(3)

#socket accept 
conn,addr=s.accept()

#socket recv
request=conn.recv(1024)

#output test
print 'request is:',request
print 'connected by :',addr

#send message
conn.sendall('OK I\'m server')
conn.close()
