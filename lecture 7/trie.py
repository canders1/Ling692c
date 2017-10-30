class Trie:
	def __init__(self,vals,start=''):
		self.val = start
		self.children = None
		for v in vals:
			self.insert(v)

	def insert(self,val):
		curr = self
		for i in range(0,len(val)):
			newcurr = Trie([val[i+1:]],val[i:i+1])
			if curr.children == None:
				curr.children = [newcurr]
			else:
				missing = True
				for c in curr.children:
					if c.val == val[i:i+1]:
						newcurr = c
						missing = False
						break
				if missing:
					curr.children.append(newcurr)
			curr = newcurr

t = Trie(["cat","cats","cast","cab"])

print t.children[0].val
for v in t.children[0].children[0].children:
	print v.val

