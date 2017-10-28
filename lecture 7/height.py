def findHeight(curr):
	if curr != None:
		h = 1
	else:
		return 0
	return h+max(findHeight(curr.leftChild),findHeight(curr.rightChild))

