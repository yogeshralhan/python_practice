
#   # File Handling !!

n = 'e1.txt'
f = open(n,'w')

try:
	f.write("hello line 1\n")                   # Method 1 to write into files
	f.write("hello line 2")
except Exception as error:
	print "error is %s " %error
finally:
	f.close()


#   #file using with method

m = 'e2.txt'
with open(m,'w') as e:
	lines = ["l1\n",							# Method 2 to write into files				
			"l2\n"
			"l3\n"	]
	e.writelines(lines)

with open(m,'r') as rf:
	for line in rf.readlines():
		print line

