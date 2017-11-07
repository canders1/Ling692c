from nltk import wsd

s1 = "I went to the bank to deposit a check."
s2 = "I sat on the bank and fished."
l = [s1,s2]
syns = []
for s in l:
	syn = wsd.lesk(s.split(), 'bank', 'n')
	print syn
	print syn.hypernyms()
	print syn.root_hypernyms()
	print syn.hyponyms()
	syns.append(syn)
print syns[0].common_hypernyms(syns[1])