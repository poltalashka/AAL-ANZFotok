# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 14:42:51 2021

@author: polta.work
"""

import glob2

filenames = glob2.glob('*.bat')  # list of all .txt files in the directory

with open('outfile.txt', 'w') as f:
    for file in filenames:
        with open(file) as infile:
            f.write(infile.read()+'\n')
#
#filenames = ['file1.txt', 'file2.txt', ...]
#with open('path/to/output/file', 'w') as outfile:
#    for fname in filenames:
#        with open(fname) as infile:
#            for line in infile:
#                outfile.write(line)