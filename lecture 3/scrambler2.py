import sys

def scrambler(word):
	grams = list(set(word[0:len(word)]))
	for i in range(0,len(word)-1):
		newgrams = []
		#print "ggrams", grams
		for g in grams:
			#print "G is:", g
			missing = unused(g,word)
			#print "Missing is: ", missing
			for m in missing:
				addgrams = permute(g,m)
				#print "Add", addgrams
				for a in addgrams:
					newgrams.append(a)
		grams = newgrams
	print newgrams

def permute(word,char):
	wordlings = []
	if word == "":
		wordlings.append(char)
	else:
		for i in range(0,len(word)+1):
			wordling = word[0:i]+char+word[i:len(word)]
			wordlings.append(wordling)
	return wordlings

def unused(word,original):
	originalList = list(original)
	wordList = list(word)
	for char in wordList:
		if char != "":
			originalList.remove(char)
	return set(originalList)

scrambler(raw_input("Please give me a word: "))
"""
for s in scrambles:
	print s
print len(scrambles)
"""