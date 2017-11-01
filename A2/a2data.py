#!/usr/bin/python
'''
Created using Python 3.6.3

How to use:
python a2data.py "C:\\Users\\KArin\\git\\EECS4314\\A2\\A2Data\\MySQL_UnderstandFileDependency.contain" "C:\\Users\\KArin\\Desktop\\School\\EECS4314\\Assignment 2" "ddl"

sys.argv[1] = .contain file
sys.argv[2] = directory of MySQL source
sys.argv[3] = keyword to search for

'''
import sys
import re
import string
import os

# open the .contain file
f = open(sys.argv[1], 'r')
for line in f.readlines():
	# get the absolute path of each file in the .contain file
	mysql_file_path = os.path.join(sys.argv[2], os.path.normpath(line.split()[-1]))
	# make sure it's a file before opening; some of them are directories
	if os.path.isfile(mysql_file_path):
		with open(mysql_file_path) as mysql_file:
			try:
				for mysql_file_line in mysql_file:
					# if the keyword is in your file, print out file to system out, then go onto the next file.
					if sys.argv[3] in mysql_file_line:
						print(mysql_file_path)
						break
			# some files give a UnicodeDecodeError when analyzing its text; skip them
			except UnicodeDecodeError:
				pass;