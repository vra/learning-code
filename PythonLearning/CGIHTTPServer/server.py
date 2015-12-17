#!/usr/bin/env python

import BaseHTTPServer
import CGIHTTPServer


HOST=''
PORT=8432

#create the server
server=BaseHTTPServer.HTTPServer((HOST,PORT),CGIHTTPServer.CGIHTTPRequestHandler)

server.serve_forever()
