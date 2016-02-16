# #Exceptions !!!


# a=7

# assert a >=10, "lower"
# print "age is %d", a


# #try except block

# try :
# 	n1= input("first num")
# 	n2= input("second num")
# 	print "result is %d" %(n1/n2)

# except ZeroDivisionError as ZeroDivided:
# 	print "error is ", ZeroDivided
	

#    # exception from files

f = open("url1.txt",'w')

try:
	f.write("#this is a comment")

except BaseException, error:
	print error


#   #raise exception explicitly

a=101
if a>100:
	raise Exception("too much")


