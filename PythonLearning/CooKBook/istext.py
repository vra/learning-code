#!/usr/bin/env python

from __future__ import division
import string

text_characters=''.join(map(chr,range(32,127)))+'\n\t\r\b'

null_trans=string.maketrans('','')

def istext(s,text_characters=text_characters,threshold=0.3):
    #if s is blank,then we think it is a text 
    if not s:
        return True

    #if s contains null,we judge it as a binary file
    if '\0' in s:
        return False

    t=s.translate(null_trans,text_characters)
    return float(len(t))/len(s) <=threshold
    

