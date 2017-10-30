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


t = Trie(["cat","cats","cast","cab"])

#print t.children[0].val
#for v in t.children[0].children[0].children:
	#print v.val
print t.get("cats").val

