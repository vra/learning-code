#!/usr/bin/env python

import SocketServer
import SimpleHTTPServer

HOST=''
PORT=8432

server=SocketServer.TCPServer((HOST,PORT),SimpleHTTPServer.SimpleHTTPRequestHandler)
server.serve_forever()
