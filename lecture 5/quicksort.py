import random

def quicksort(l):
	if len(l) < 2:
		return l
	else:
		l,p = partition(l)
		print "Calling with pivot", p
		print l
		print "q1",quicksort(l[0:p+1])
		print "q2",quicksort(l[p+1:len(l)])
		newl = quicksort(l[0:p+1])+quicksort(l[p+1:len(l)])
		print "q+",newl
		return newl

def partition(l):
	pivot = 0
	i = 0
	j = len(l)-1
	while i < j:
		print pivot
		print 'val p', l[pivot]
		print i
		print j
		print "val i", l[i]
		print 'val j', l[j]
		if l[i] > l[pivot] and l[j] < l[pivot]:
			oldj = l[j]
			oldi = l[i]
			l[i] = oldj
			l[j] = oldi
		else:
			if l[i] <= l[pivot]:
				i = i+1
			if l[j] >= l[pivot]:
				j = j-1
	return l,j

print quicksort([9,10,2,4,7,9,10,2,3])