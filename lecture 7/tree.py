from nltk.tree import *

t = Tree(1, [2, Tree(3, [4]), 5])
print(t)
t.insert(3,4)

print(t)

