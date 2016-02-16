
p='e3.txt'
with open(p,'w') as fil:
	fil.write("something for the demo")

file_content= ''

with open(p,'r') as ready:
	#file_content= ready.readlines()              #   readlines : will display the entire as single string
	file_content= ready.read()  				  #   read :  weill display char by char
	for line in file_content:
		print line

