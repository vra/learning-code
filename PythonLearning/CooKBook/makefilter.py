#!/usr/bin/env python

import string

allchars=string.maketrans('','')

def makefiter(keep):
    delchars=allchars.translate(allchars,keep)
    
    def filter(words):
        return words.translate(allchars,delchars)
    return filter


#test
p=makefiter('aeiouy')
print ('i love you and this always is true.')
print p('i love you and this always is true.')

