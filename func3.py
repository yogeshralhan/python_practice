

def html(text,tag):
	return '<%s>%s</%s>' %(tag,text,tag)
while 1:
	r=raw_input("continue Y/N?")
	if r=='y' or r=='Y':
		p= raw_input("enter your text")
		q=raw_input("enter your tag")
		print html(p,q)
	else:
		break	

