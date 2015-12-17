#!/usr/bin/env python

import pickle

#define class
class Person(object):
    Name=""
    age=0;

#dump an object
wang=Person();
str_wang=pickle.dumps(wang)

#test output
#print type(str_wang)
#print str_wang

#load object
obj_wang=pickle.loads(str_wang)
#after load,the obj_wang is a object of class Person,just same as wang
#you can do everything on obj_wang just like on wang

#test result
#print type(obj_wang)
#print obj_wang   
print obj_wang.age
