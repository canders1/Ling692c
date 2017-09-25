import sys

char = sys.argv[1]
height = int(sys.argv[2])
which = sys.argv[3]

if which == "0":
	start = char
	print start
	for i in range(1,height):
		start = start+char+char
		print start
else:
	start = char
	for i in range(1,height):
		start = " "+start
	print start
	for i in range(1,height):
		start = start[1:]+char+char
		print start
