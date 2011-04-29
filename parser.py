#!/usr/bin/env python

import Hashtable

file = open("input.txt",'r')

lines = file.readlines()
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


