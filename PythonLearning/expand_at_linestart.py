#!/usr/bin/env python

def expand_at_linestart(P,tablen=24):
    import re
    def exp(mo):
        return mo.group().expandtabs(tablen)
    return ''.join([re.sub(r'^\s+',exp,s) for s in P.splitlines(True)])

print expand_at_linestart('''
   thiwososof
weoro
   weoorjo
owoero'''
)

