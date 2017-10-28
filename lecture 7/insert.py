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
