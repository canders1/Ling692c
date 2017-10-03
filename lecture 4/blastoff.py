def countDown(n): #A recursive function that prints a countdown from n to "Blast off!"
  if n == 0:
    print "Blast off!"
    countDown(n-1) 
  else:
    print n
    countDown(n-1)
countDown(10)