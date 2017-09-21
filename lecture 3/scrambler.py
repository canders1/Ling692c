import sys

def scrambler(word):
	scrambles = [""]
	for i in range(0,len(word)):
		print "iteration: ", i
		newscrambles = []
		for w in scrambles:
			wList = list(w)
			missingList = list(word)
			print "Miss", missingList
			for char in wList:
				if char != "":
					missingList.remove(char)
			print "issing: ", missingList
			print missingList
			missing = set(missingList)
			print missing
			for j in missing:
				print "j", j
				newscrambles.append(w+j)
		scrambles = newscrambles
		print scrambles
	return scrambles

scrambles = scrambler(raw_input("Please give me a word: "))
for s in scrambles:
	print s
print len(scrambles)