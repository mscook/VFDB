# Mitchell Jon Stanton-Cook
# m.stantoncook@gmail.com

import textwrap
import sys

ident = sys.argv[1]

with open(ident+".dat") as fin:
    lines = fin.readlines()

with open(ident+".fa") as fin2:
    lines2 = fin2.readlines()

seq = ''
for l in lines2:
    if l.find('>') == -1:
        seq = seq + l.strip()

location = lines[0].strip().split(",")[1:]
ori = lines[1].strip().split(',')[1:]

counter = 1
for l in lines[1:]:
    allele = l.split(',')[0].strip()
    new = list((seq+'x')[:-1])
    changes = l.strip().split(',')[1:]
    for index, loc in enumerate(location):
        if changes[index] == '-':
            replace = ori[index]
        else:
            replace = changes[index]
        new[int(loc)-1] = replace
    tmp = ''.join(new)
    new = textwrap.wrap(tmp.upper(), 70)
    print '>'+ident+'-'+str(allele)
    counter = counter+1
    for e in new:
        print e
