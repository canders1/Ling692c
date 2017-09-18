"""
Author: Carolyn Anderson
Date: 9/15/17

This is a word-count program. 

Input: 	a list of words to count; 
		a filename containing text to search
Output: a count per word of how many times the word occurs
"""
import sys
from collections import defaultdict

def main():

	wordname = sys.argv[1] #Get words to count
	textname = sys.argv[2] #Get text to search

	wordfile = file(wordname, "r")
	textfile = file(textname, "r")
	words = wordfile.read()
	text = textfile.read()

	wordList = words.split("\n") #Split word file into a list
	counts = wordcount(text)
	printResults(counts,wordList)

###############################################################

#Produces a dictionary containing token counts for each word in text

def wordcount(text): 	#We name the arguments to the function in the parentheses
  textList = text.split(" ")
  d = defaultdict(int)
  for t in textList:
    old = d[t]
    d[t] = old+1
  return(d)

###############################################################

#Prints the word counts found in counts for each white-space separated word in wordString

def printResults(counts,words):
	for w in words:
		w = w.strip()
		if w in counts:
			print w, counts[w]
		else:
			print w, 0

###############################################################

main()