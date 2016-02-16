# def peop(m,*arg):
# 	print m
# 	total=0
# 	for n in arg:
# 		total=total+n
# 	return total

# print peop("sum =",1,2,3,4)


def try1(n):
	if n==0:
		return 0
	return try1(n-1) + n
for n in range(5):
	print try1(n)