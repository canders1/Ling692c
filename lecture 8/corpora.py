import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

for s in gutenberg.sents('austen-emma.txt')[0:10]:
	print " ".join(s)

emma = Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print emma.concordance("knightley")
emma.dispersion_plot(["she","he","Knightley","Emma","money","Elton"])
emma.plot(30)
emma.similar("Knightley")

s = " ".join(gutenberg.sents('austen-emma.txt')[0])
tokens = nltk.word_tokenize(s)
print tokens
tagged = nltk.pos_tag(tokens)
print tagged
entities = nltk.chunk.ne_chunk(tagged)
print entities
