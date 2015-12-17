#!/usr/bin/env python

import os
import multiprocessing
import time

#define the method of input contents to queue
def inputQ(queue):
	info=str(os.getpid())+'put:'+str(time.time())
	queue.put(info)

#define the method of get contents from queue
#in order to avoid stdout mass,we use a lock 
def outputQ(queue,lock):
	info=queue.get()	
	lock.acquire()
	print(str(os.getpid())+'get:'+info)
	lock.release()

#main part 
if __name__=='__main__':
	record1=[]	
	record2=[]	
	lock=multiprocessing.Lock()
	#3 implies that can allow 3 processes to put content to queue maximally
	queue=multiprocessing.Queue(3)

	#input process
	for i in range(10):
		process=multiprocessing.Process(target=inputQ,args=(queue,))
		process.start()
		record1.append(process)

	#output process
	for i in range(10):
		process=multiprocessing.Process(target=outputQ,args=(queue,lock))
		process.start()
		record2.append(process)

	for p in record1:
		p.join()

	#close the queue,since all input processes have been finished
	queue.close()

	for p in record2:
		p.join()	
