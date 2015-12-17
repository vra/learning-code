#!/usr/bin/env python

import signal

#Define signal process function
def myHandler(s,f):
    print('I received:',s)

#register signal.SIGSTP's handler
signal.signal(signal.SIGTSTP,myHandler)
signal.pause()

print 'end of the signal test'

