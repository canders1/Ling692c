def flatten(lis):
    """Given a list, possibly nested to any level, return it flattened."""
    new_lis = []
    for item in lis:
        if type(item) == type([]):
            new_lis.extend(flatten(item))
        else:
            new_lis.append(item)
    return new_lis

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

	def getValues(self):
		v = []
		for c in self.children:
			v.append(c.val)
		return v

	def get(self,val):
		curr = self
		for i in range(0,len(val)+1):
			if i == len(val):
				return curr
			if curr.children==None:
				return False
			else:
				missing = True
				for c in curr.children:
					if c.val == val[i:i+1]:
						missing = False
						curr = c
						break
					if missing:
						return False

	def getLeaves(self,pre=''):
		pre = pre + self.val
		if self.children == None:
			return [pre]
		else:
			pres = []
			for c in self.children:
				pres.append(c.getLeaves(pre))
			return flatten(pres)

t = Trie(["cat","cats","cast","cab"])
print t.children[0].children[0].children[2].val
pres = t.getLeaves()
print pres

					

