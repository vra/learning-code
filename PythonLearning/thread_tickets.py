#!/usr/bin/env python

"This is a simple simulation of multi-thread tickets selling system"


import threading
import os

def doOtherCriticalJob():
    print 'I am in other ciritcal job'

def doNonCriticalJob():
    print 'I am in non-ciritcal job'

def doJob(tid):
    global i
    global lock

    while True:
        lock.acquire()
        if i!=0:
            i=i-1
            print(tid,'now left',i)
            doOtherCriticalJob()
        else:
            print('Thread_id:',tid,"No more tickets")
            os._exit(0)

        lock.release()
        doNonCriticalJob()


#define global variables
i=256
lock=threading.Lock()

#start 16 threads
for k in range(10):
    new_thread=threading.Thread(target=doJob,args=(k,))
    new_thread.start()



        
