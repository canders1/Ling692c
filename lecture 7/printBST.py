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
		printBST(r,ind-1)
	if l != None:
		printBST(l,ind-1)

