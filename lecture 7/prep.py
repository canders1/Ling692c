from nltk.corpus import gutenberg
import re

emma = " ".join(gutenberg.words('austen-emma.txt')[10000:11000])
emma = re.sub(r"[0-9,\.\(\):;\"\'\-\!\?`_]","",emma)	
emma = emma.split(" ")
emma = map(lambda x:x.lower(),emma)
for i in emma:
	print i