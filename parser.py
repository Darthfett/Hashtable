#!/usr/bin/env python

import Hashtable
import sys
args = sys.argv
args.pop(0)
if len(args) != 1:
    print "Invalid number of arguments.  Please call with the path to exactly one file."
    sys.exit(1)

file = open(args.pop(0),'r')

lines = file.readlines()

file.close()
line_count = int(lines.pop(0).strip())

insert_values = [int(line.strip()) for line in lines[:line_count]]
search_value = int(lines[line_count].strip())

hashtables = [Hashtable.ChainedHashtable(), Hashtable.LinearHashtable(), Hashtable.QuadraticHashtable(), Hashtable.DoubleHashtable()]

for table in hashtables:
    for value in insert_values:
        table.insert(value)

files = [open("chain.txt",'w'), open("linear.txt",'w'), open("quadratic.txt",'w'), open("double.txt",'w')]


for i in range(len(files)):
    files[i].write(str(hashtables[i]))
    files[i].write("\n-1\n")
    files[i].write(hashtables[i].search(search_value) + "\n")
    files[i].close()
