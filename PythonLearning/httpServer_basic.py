#!/usr/bin/env python

import socket

#address
HOST=''
PORT=8432

#make response sentences
text_content='''HTTP/1.x 200 OK
Content-Type:text/html

<head>
<title>
Simple HTTP Server via Python
</title>
</head>
<html>
<p>
    Does this picture is your wanting?
</p>
<img src="test.jpg"/>
</html>
'''
#read the picture and transport it in a way of binary format
f=open('test.jpg','rb')
picture_content='''
HTTP/1.x 200 OK
Content-Type:image/jpg

'''
picture_content+=f.read()
f.close()

#configure socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

while True:
    s.listen(3)
    conn,addr=s.accept()
    request=conn.recv(1024)
    method=request.split(' ')[0]
    src=request.split(' ')[1]

    #deal with the request
    if method=='GET':
        if src=='/test.jpg':
            content=picture_content
        else:
            content=text_content

        print 'connected by ',addr
        print 'request is ',request
        conn.sendall(content)
    
    #close the connection 
    conn.close()


