import nltk
from nltk.corpus import gutenberg
from nltk.text import Text

emma = Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
fdist = nltk.FreqDist(emma)

#50 most frequent words:
for word, frequency in fdist.most_common(50):
    print(u'{};{}'.format(word, frequency))

#Words that only occur once:
print fdist.hapaxes()

#Word use over time in text:
emma.dispersion_plot(["she","he","Knightley","Emma","money","Elton"])

#Most frequent 30 words:
emma.plot(30)

#Words that are similar to "Knightley":
emma.similar("Caroline")
