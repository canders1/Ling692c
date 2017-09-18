import sys

wordname = sys.argv[1]
textname = sys.argv[2]

wordfile = file(wordname, "r")
textfile = file(textname, "r")
words = wordfile.read()
text = textfile.read()

wordList = words.split("\n")

print wordList
print text
