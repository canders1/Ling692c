import nltk
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

emma = Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.dispersion_plot(["she","he","Knightley","Emma","money","Elton"])
emma.plot(30)
emma.similar("Knightley")