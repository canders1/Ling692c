def flatten(lis):
    """Given a list, possibly nested to any level, return it flattened."""
    new_lis = []
    for item in lis:
        if type(item) == type([]):
            new_lis.extend(flatten(item))
        else:
            new_lis.append(item)
    return new_lis

class Node:
    def __init__(self, val):
        self.val = val
        self.children = None

class Trie:
	def __init__(self,vals):
		self.val = ""
		self.children = None
		for v in vals:
			self.insert(v)

	def insert(self,val):
		curr = self
		for i in range(0,len(val)):
			newcurr = Node(val[i:i+1])
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

def printLeaves(curr,pre):
	pre = pre + curr.val
	if curr.children == None:
		return pre
	else:
		pres = []
		for c in curr.children:
			pres.append(printLeaves(c,pre))
		return flatten(pres)

t = Trie(["cat","cats","cast","cab"])

pres = printLeaves(t,"")
print pres

					

