#!/usr/bin/python
'''
Created using Python 2.7.13

How to use:
	python include.py <input-folder-path> <output-file-name>
	(ex. python include.py ".../mysql-server-mysql-8.0.2" "test.raw.ta")
	(ex. python include.py "C:\\Users\\KArin\\Desktop\\School\\EECS4314\\Assignment 2\\mysql-server-mysql-8.0.2" "C:\\Users\\KArin\\git\\EECS4314\\A3\\a3data\\test.raw.ta"

	NOTE: the output-file-name must exist.
'''

import os
import sys

file_ta = open(sys.argv[2], "w")

for root, dirs, files in os.walk(sys.argv[1], topdown=False):
    for name in files:
        if name[-3:] == ".cc" or name[-2:] == ".h":
            lines = open(os.path.join(root, name), "r")
            for line in lines:
                if line[:8] == "#include":
                    string = "{} -> {}\n".format(name, line[10:-2])
                    file_ta.write(string)
file_ta.close()


