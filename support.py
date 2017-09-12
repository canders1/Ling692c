from nltk import misc

words = ["regex","algorithm","semantics","modeling","cognition","neural","connectionist","parsing","syntax","tagging"]
grid, searchList = misc.wordfinder.wordfinder(words, rows=20, cols=20, attempts=50, alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print grid
#print searchList