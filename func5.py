#Regular Expressions

import re
def find(pat,text):
	match=re.search(pat,text)
	if match:
		print match.group()
	else:
		print "not found"

find('iz','fiizzz')
find('...l','hello')
find('\s\d+\s\d','hello its 12 2')
find('\w+\s+\w\.','this isthe gmail')

#print (re.split(r'(s*)','hello sim fine'))
#print (re.split(r'[a-f]','adjdgdfjsdnAsjiASCNNF'),re.I|re.M)
# print (re.findall(r'\d','hello123 main 323kf'))
# print (re.findall(r'\d{1,4}\s\w+','please123456 main23 in '))
print (re.findall(r'\w+\s\w+\s\d{1,4}','popularity in 1990 is good'))