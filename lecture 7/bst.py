class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

class BST:
    def __init__(self, vals):
        if len(vals) == 0:
        	self.root = None
        else:
        	self.root = Node(vals.pop(0))
        	while len(vals) > 0:
        		i = vals.pop(0)
        		curr = self.root
        		searching = True
        		while searching:
        			if i > curr.val:
        				if curr.rightChild == None:
        					curr.rightChild = Node(i)
        					searching = False
        				else:
        					curr = curr.rightChild
        			elif i < curr.val:
        				if curr.leftChild == None:
        					curr.leftChild = Node(i)
        					searching = False
        				else:
        					curr = curr.leftChild
        			else:
        				searching = False

def printBST(curr,ind):
	print ind+str(curr.val)
	r = curr.rightChild
	l = curr.leftChild
	if r != None:
		printBST(r,ind+ind)
	if l != None:
		printBST(l,ind+ind)

def prettyPrintBST(curr,ind):
	tab = ' '*ind
	print tab+str(curr.val)+tab
	r = curr.rightChild
	l = curr.leftChild
	if r != None:
		prettyPrintBST(r,ind+2)
	if l != None:
		prettyPrintBST(l,ind-2)

def findHeight(curr):
	if curr != None:
		h = 1
	else:
		return 0
	return h+max(findHeight(curr.leftChild),findHeight(curr.rightChild))

def insertBST(curr,i):
	if curr == None:
		return BST([Node(i)])
	if i > curr.val:
		if curr.rightChild == None:
			curr.rightChild = Node(i)
		else:
			insertBST(curr.rightChild,i)
	elif i < curr.val:
		if curr.leftChild == None:
			curr.leftChild = Node(i)
		else:
			insertBST(curr.leftChild,i)
	else:
		pass

def inOrder(curr):
	l = curr.leftChild
	r = curr.rightChild
	lst = [curr.val]
	if l != None:
		lst=inOrder(l)+lst
	if r !=None:
		lst=lst+inOrder(r)
	return lst

b = BST([0,1,2,5,-6,-1,-1,3,-2,4])
#print b.root.val
#print b.root.leftChild.val
#print b.root.rightChild.val
#print b.root.rightChild.rightChild.val
#print b.root.rightChild.rightChild.rightChild.val
#printBST(b.root," ")
#print
#prettyPrintBST(b.root,12)
#print
#print findHeight(b.root)
insertBST(b.root,-4)
prettyPrintBST(b.root,2*findHeight(b.root))
print inOrder(b.root)