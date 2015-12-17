#!/usr/bin/env python 

"This is a program of tickets selling using object-oriented programming method "

import threading
import os

class BoothThread(threading.Thread):
    def __init__(self,tid,monitor):
        self.tid=tid
        self.monitor=monitor
        threading.Thread.__init__(self)
    def run(self):
        while True:
            monitor['lock'].acquire()
            if monitor['ticket']!=0:
                monitor['ticket']=monitor['ticket']-1
                print('Thread_id:',self.tid,'now left:',monitor['ticket'])

                #do some other critical jobs
            else:
                print('Thread_id:',self.tid,'no more tickets')
                os._exit(0)
            monitor['lock'].release()
            #do some non-critical jobs

#set parameters
monitor={'ticket':100,'lock':threading.Lock()}

#start 10 threads
for k in range(10):
    new_thread=BoothThread(k,monitor)
    new_thread.start()



