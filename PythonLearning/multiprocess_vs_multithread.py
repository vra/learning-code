#!/usr/bin/env python


import os
import threading
import multiprocessing

#define work function
def doJob(type,lock):
    lock.acquire()
    print(type,os.getpid())
    lock.release()

#begin main process
print('main',os.getpid())

#multi-thread
record=[]
lock=threading.Lock()
for i in range(10):
    new_thread=threading.Thread(target=doJob,args=('thread',lock))
    new_thread.start()
    record.append(new_thread)

#wait other processes(actually for multi-thread,this is not necessary,cause there is only one process)
for t in record:
    t.join()

#multi-process
record=[]
lock=multiprocessing.Lock()
for i in range(10):
    new_process=multiprocessing.Process(target=doJob,args=('process',lock))
    new_process.start()
    record.append(new_process)

for p in record:
    p.join()



