#!/usr/bin/env python

import multiprocessing 

#define process1-send words from a end of pipe
def proc1(pipe):
 	pipe.send('hello,I am at one end of PIPE')	
 	print('proc1:recv',pipe.recv())

def proc2(pipe):
	print("proc2:recv:",pipe.recv())
	pipe.send('hello,too')

#There is a question must be complained:when use Windows,
#and you select precompile when you install python(then 
#system will generate a .pyc file in order to acceleration)
#when doing this,if you don't use "__name__=='__main__'",then
#your program will crash.so use this fromat is a good choice
if __name__=='__main__':
	#build a pipe
	pipe=multiprocessing.Pipe()

	#pass one end to proc1
	p1=multiprocessing.Process(target=proc1,args=(pipe[0],))
	#pass another end to proc2
	p2=multiprocessing.Process(target=proc2,args=(pipe[1],))

	#begin processes
	p1.start()
	p2.start()
	p1.join()
	p2.join()
