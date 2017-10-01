import re

def main():
	f1 = file("onsets.txt", "r")
	f2 = file("good_onsets.txt", "r")
	onsets = f1.read().split("\n")
	good = f2.read().split("\n")
	r = re.compile(r'^[bdgptk]*[zv(th)fchs(sh)]*[mn]*[rl]*[yjw]*[aeiou]+')
	valid = []
	for word in onsets:
		ans = search(r,word)
		if ans:
			valid.append(ans)
	for v in valid:
		if v not in good:
			print v,"is incorrect"
		else:
			good.remove(v)
	print "Missing:"
	for g in good:
		print g

def search(r,line):
	res = re.search(r,line)
	if res is not None:
		return line
	else:
		return False

main()