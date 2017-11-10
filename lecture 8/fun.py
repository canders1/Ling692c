from nltk import misc
from nltk import chat

misc.chomsky.generate_chomsky(times=5, line_length=72)

words = ["CHOMSKY","SYNTAX","SEMANTICS","PHONEME","LEXICON"]
words, puzzle = misc.wordfinder.wordfinder(words, rows=10, cols=10, attempts=50, alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for w in words:
	print " ".join(w)
print puzzle

chat.zen.demo()