#!/usr/bin/env python

import pickle

#define class
class Person(object):
    name=''
    age=0

filename='wang.pk'

#load packing file
with open(filename,'r') as file:
    wang=pickle.load(file)

#test loaded object
print wang.age

