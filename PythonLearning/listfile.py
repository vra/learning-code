#!/usr/bin/env python
#-*- coding:utf-8 -*-
"This is a tool works like the program 'tree',i.e.,show the files in particual directory"
import os
import glob

def ListFile(filename,count):
    if not os.path.exists(filename):
        print 'File not exists!'
        return 
    if os.path.isfile(filename):
        file=os.path.basename(filename)

        #in order to a neaty show,we add '|' at first,but there is also some bugs
        print '\t'*(count-1)+'|'+'\t'*count+'|--'+file
        return
    elif os.path.isdir(filename):
        print '\t'*(count-1)+'|'+'\t'*count+'|--'+filename
        containedFiles=glob.glob(filename+'/*')
        for file in containedFiles:
           ListFile(file,count+1)


#ListFile('/home/wang/Src/mysite',1)
