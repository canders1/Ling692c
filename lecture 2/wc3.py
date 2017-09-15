"""
Author: Carolyn Anderson
Date: 9/15/17

This is a word-count program. 

Input: 	a list of words to count; 
		a filename containing text to search
Output: a count per word of how many times the word occurs
"""

from collections import defaultdict

def main():

	print "Hello! This is a word count program."

	quit = False
	while quit == False:
		print "Please pick an option: "
		print "1. Run word count"
		print "2. Quit"
		choice = int(raw_input("Your choice is: ")) #Remember to convert the input to an integer if you're comparing it to an integer!
		if choice == 2:
			print "Goodbye!"
			quit = True
		else:
			filename = raw_input("File name: ")
			f = file(filename,"r")
			text = f.read()
			wordString = raw_input("Words to count: ")
			counts = wordcount(text)
			printResults(counts,wordString)

###############################################################

#Produces a dictionary containing token counts for each word in text

def wordcount(text): 	#We name the arguments to the function in the parentheses
  text = "It was the best of times, it was the worst of times."
  textList = text.split(" ")
  d = defaultdict(int)
  for t in textList:
    old = d[t]
    d[t] = old+1
  return(d)

###############################################################

#Prints the word counts found in counts for each white-space separated word in wordString

def printResults(counts,wordString):
	words = wordString.split(",")
	for w in words:
		w = w.strip()
		if w in counts:
			print w, counts[w]
		else:
			print w, 0

###############################################################

main()