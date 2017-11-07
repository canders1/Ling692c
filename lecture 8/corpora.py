import nltk
from nltk.corpus import gutenberg
from nltk.text import Text

#Get first 10 sentences of Emma
for s in gutenberg.sents('austen-emma.txt')[0:10]:
	print " ".join(s)

#Get all words in Emma
emma = Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#Search for sentences containing "knightley"
print emma.concordance("knightley")