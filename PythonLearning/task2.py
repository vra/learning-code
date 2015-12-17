#!/usr/bin/env python

#This is python task on the page http://www.cnblogs.com/vamei/archive/2012/10/26/2741702.html

import random

#get 5 integers from 1 to 22 randomally
seq1=random.sample(range(1,23),5)

#test result
#print seq1

#make a 8-digital number,every digital is between 1 and 6
str_num=''
for i in range(8):
    str_num=str_num+str(random.choice(range(1,7)))
#another good way:change random.choice(range(1,7)) to random.randomint(1,6)

#change str to int
num=int(str_num)
#test result
#print num
