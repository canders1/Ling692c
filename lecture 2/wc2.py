from collections import defaultdict

###############################################################

def wordcount(text): 	#We name the arguments to the function in the parentheses
  textList = text.split(" ")
  d = defaultdict(int)
  for t in textList:
    old = d[t]
    d[t] = old+1
  return(d)
###############################################################

text = "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort."
counts = wordcount(text)
print(counts)