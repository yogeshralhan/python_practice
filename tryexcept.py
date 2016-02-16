
# try:
#     x = int(raw_input("Please enter a number: "))
# except ValueError:
#   	print "Oops!  That was no valid number.  Try again..."


try:
	f=open('file1.txt','r')
	text= f.read()
	
	print text

except IOError:
	print "ioerror",file1.txt