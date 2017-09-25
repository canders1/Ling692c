import re
import sys

expr = re.compile(sys.argv[1]) #Compile command-line arg into regex
f = file(sys.argv[2],"r") #Open file using command-line arg
phoneList = f.read().split('\n') #Read in phone numbers and split on newline character

allList = [] #Phone numbers
correctList = [] #Correct results
for i in phoneList: 
  phone = i.split(',')
  if phone[1] == 'good':
    correctList.append('good')
  elif phone[1] == 'bad':
    correctList.append('bad')
  allList.append(phone[0])

results = [] #Now test out the regex!
for phone in allList:
  r = re.search(expr,phone)
  if r is None:
    results.append("bad")
  else:
    results.append("good")

count = 0.0 #Calculate a score
wrongList = [] #Keep track of problem phone numbers
for r in range(0,len(results)):
  if results[r] == correctList[r]:
    count = count+1.0
  else:
    wrongList.append(r)
total = count/float(len(results))
print "Your score was: ", total
print "Here are phone numbers you failed on: "
for w in wrongList:
  print allList[w]