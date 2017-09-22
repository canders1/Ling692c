

def main(ws):
	plist = normList(ws)
	pairs = []
	for i in range(0,len(plist)-1):
		if plist[i][1] == plist[i+1][1]:
			pairs.append((plist[i][0],plist[i+1][0]))
	for p in pairs:
		print p[0], p[1]

def normList(wordlist):
	pairlist = []
	for w in wordlist:
		wlist = list(w)
		wlist.sort()
		wpair = (w,wlist)
		pairlist.append(wpair)
	pairlist.sort(key=lambda w: w[1])
	return pairlist

main(["cra","rat","car","art"])
