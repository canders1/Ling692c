from nltk.corpus import gutenberg
import re
import trieClass
import sys

def checkSpelling(word,trie):
	return trie.get(word)

def checkText(text,trie):
	misspellings = []
	for i in range(0,len(text)):
		if checkSpelling(text[i],trie):
			pass
		else:
			misspellings.append(text[i])
			text[i] = '#'+text[i]+'#'
	return misspellings

def main():
	emma = " ".join(gutenberg.words('austen-emma.txt')[0:10000]) #text preprocessing
	emma = re.sub(r"[0-9,\.\(\):;\"\'\-\!\?`_]","",emma)	
	emma = emma.split(" ")
	emma = map(lambda x:x.lower(),emma)

	t = trieClass.Trie(emma)	#Create a trie with first 10,000 words of Emma

	f = file(sys.argv[1], 'r')
	text = f.readlines()
	text = map(lambda x:x.strip('\n'),text)
	for c in checkText(text,t):
		print c
	print text
main()
