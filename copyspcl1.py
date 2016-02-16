import re
import os
import commands
import sys
import shutil


print "Listing all the special file names:---->"

def special_path(dirname):
	result=[]
	paths = os.listdir(dirname)
	for fname in paths:
		match=re.search(r'(\w+)__(\w+)__\.(\w+)',fname)
		if match:
			result.append(os.path.abspath(os.path.join(dirname,fname)))
	print result
	return result

special_path("/home/yogesh/Documents/pc_docs/google-python-exercises/copyspecial")


print "Copy all of the given files to the given dir:----->"
	
def copy_to(path,to_dir):
	
	if not os.path.exists(to_dir):
		os.mkdir(to_dir)
	paths = special_path("/home/yogesh/Documents/pc_docs/google-python-exercises/copyspecial")

	for path in paths:
		fname = os.path.basename(path)
		shutil.copy(path,os.path.join(to_dir , fname))

copy_to("/home/yogesh/Documents/pc_docs/google-python-exercises/copyspecial","/home/yogesh/Documents/pc_docs/Tutorial Codes")