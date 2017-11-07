from nltk.sentiment import vader
from nltk.corpus import gutenberg
from nltk.text import Text
from nltk.sentiment import util

analyzer = vader.SentimentIntensityAnalyzer(lexicon_file='sentiment/vader_lexicon.zip/vader_lexicon/vader_lexicon.txt')
for s in gutenberg.sents('austen-emma.txt')[0:12]:
	emma = " ".join(s)
	print emma
	print analyzer.polarity_scores(emma)
	print " ".join(util.mark_negation(emma.split(), double_neg_flip=False, shallow=False))
