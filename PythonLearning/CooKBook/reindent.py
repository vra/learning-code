#!/usr/bin/env python

def reindent(s,numspace):
    space=numspace*' '
    #use strip to get beginning space off
    lines=[space+ line.strip() for line in s.splitlines()]
    return '\n'.join(lines)

s='''
hello erver
  wowoe
helwo
   woeoerjo
weorjo 
        woweorj
'''
print reindent(s,4)
print reindent(s,14)
