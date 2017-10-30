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
		self.root = Node("")
		for v in vals:
			self.insert(v)

	def insert(self,val):
		curr = self.root
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


t = Trie(["cat","cats","cast","cab"])

print t.root.children[0].val
for v in t.root.children[0].children[0].children:
	print v.val
					

