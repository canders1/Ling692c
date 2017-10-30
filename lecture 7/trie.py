class Node:
    def __init__(self, val):
        self.val = val
        self.children = None

class Trie:
	def __init__(self,vals):
		self.root = Node("")
		for v in vals:
			curr = self.root
			for i in range(0,len(v)):
				newcurr = Node(v[i:i+1])
				if curr.children == None:
					curr.children = [newcurr]
				else:
					missing = True
					for c in curr.children:
						if c.val == v[i:i+1]:
							newcurr = c
							missing = False
							break
					if missing:
						curr.children.append(newcurr)
				curr = newcurr

t = Trie(["cat","cats","cast","cab"])
print t.root.val
print t.root.children[0].val
for v in t.root.children[0].children[0].children:
	print v.val


					

