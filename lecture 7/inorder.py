def inOrder(curr):
	l = curr.leftChild
	r = curr.rightChild
	lst = [curr.val]
	if l != None:
		lst=inOrder(l)+lst
	if r !=None:
		lst=lst+inOrder(r)
	return lst
