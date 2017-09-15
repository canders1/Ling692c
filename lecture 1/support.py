from nltk import misc

words = ["regex","algorithm","semantics","modeling","cognition","neural","connectionist","parsing","syntax","tagging"]
grid, searchList = misc.wordfinder.wordfinder(words, rows=20, cols=20, attempts=50, alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ')

"""
total = ""
for i in grid:
	line = ""
	for j in i:
		line = line+j
	total = total +","+line
print total

"""
words = ""
for s in searchList:
	words = s+","+words
print words