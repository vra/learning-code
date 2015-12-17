#!/usr/bin/env python

import pickle

#define class
class Person(object):
    name=''
    age=0;

wang=Person();
filename="wang.pk"

#open file with write-mode
with open(filename,'w') as file:
    #serialize and save object
    str_wang=pickle.dump(wang,file);
