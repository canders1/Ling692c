"""
Author: Carolyn Anderson
Date: 9/25/17

Prints out a pyramid of characters specified by the user.

Input: char: character to be printed
		height: number of lines in pyramid
		which: left-slanted or centered pyramid
"""

import sys

def main():

	char = sys.argv[1]
	height = int(sys.argv[2])
	which = sys.argv[3]

	if which == "0": #Left-leaning pyramid
		start = char
		print start
		for i in range(1,height):
			start = start+char+char
			print start
	else: #Centered pyramid
		start = char
		for i in range(1,height):
			start = " "+start
		print start
		for i in range(1,height):
			start = start[1:]+char+char
			print start
main()
