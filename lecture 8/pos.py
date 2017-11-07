import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

s = " ".join(gutenberg.sents('austen-emma.txt')[0])
tokens = nltk.word_tokenize(s)
tagged = nltk.pos_tag(tokens)
print tagged
