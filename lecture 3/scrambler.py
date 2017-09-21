import sys

def scrambler(word):
	scrambles = [""]
	for i in range(0,len(word)):
		newscrambles = []
		for w in scrambles:
			wList = list(w)
			missingList = list(word)
			for char in wList:
				if char != "":
					missingList.remove(char)
			missing = set(missingList)
			for j in missing:
				newscrambles.append(w+j)
		scrambles = newscrambles
	return scrambles

scrambles = scrambler(raw_input("Please give me a word: "))
for s in scrambles:
	print s
print len(scrambles)