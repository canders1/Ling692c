import sys

def scrambler(word):
	if len(word) == 1:
		nstrings = [word]
		return nstrings
	else:
		uniqueList = list(word)
		finals = []
		print "UniqueList", uniqueList
		char = uniqueList[0]
		tail = ''.join(uniqueList[1:])
		nstrings = list(set(scrambler(tail)))
		print nstrings
		for n in nstrings:
			for i in range(0,len(n)+1):
				newfinal = n[0:i]+char+n[i:len(n)]
				finals.append(newfinal)
		return list(set(finals))

scrambles = scrambler(raw_input("Please give me a word: "))
for s in scrambles:
	#print s
print len(scrambles)