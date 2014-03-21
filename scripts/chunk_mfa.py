#!/usr/bin/env python

import sys
import textwrap

"""
Usage:

python chunk_mfa.py input.fa 500 > outname.fa

Mitchell Stanton-Cook (m.stantoncook@gmail.com)
2013
"""


def chunk(l, n=500):
    """
    Yield successive n-sized chunks from l.
    """
    return [l[i:i+n] for i in range(0, len(l), n)]


with open(sys.argv[1]) as fin:
    lines = fin.readlines()
    chunk_size = int(sys.argv[2])

for i in range(0, len(lines)):
    if lines[i].startswith('>'):
        counter = 1
        name = lines[i].strip()[1:]
        pos = i+1
        cur = ''
        try:
            while not lines[pos].startswith('>'):
                cur = cur+lines[pos].strip()
                pos = pos+1
        except IndexError:
            pass
        cur = cur.replace('N','')
        chunked = chunk(cur, chunk_size)
        for index, c in enumerate(chunked):
            print '>'+name+"_"+str(index+1)+", "+name+"_"+str(index+1)+        \
                                ", , Ec958 ["+name+"]"
            new = textwrap.wrap(c.upper(), 80)
            for e in new:
                print e
