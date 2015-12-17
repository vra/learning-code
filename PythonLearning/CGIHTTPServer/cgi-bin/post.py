#!/usr/bin/env python

import cgi
form=cgi.FieldStorage()

#output to stdout,CGIHTTPServer will take these as reponse to client
print 'Content-Type:text/html'
print 
print '<p>Hello,World!</p>'
print "<p>"+repr(form['firstname'])+"</p>"

