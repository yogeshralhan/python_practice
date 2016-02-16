

def vovels(strings):
	v = 'aeiou'
	str = ''

	for char in strings:
		if char not in v:
			str +=char
	return str

s= raw_input("enter ur string")
print type(s)

ty= vovels(s)
print ty