name = raw_input("Please choose a cat name:\n")

if (name != "Captain Haddock") and (name != "Calvin"):
  print "That's not my cat!"
  name2 = raw_input("Please choose another cat name:\n")
  if (name2 != "Captain Haddock") and (name2 != "Calvin"):
    print "That's not my cat!"
    name3 = raw_input("Please choose another cat name:\n")
    if(name2 != "Captain Haddock") and (name2 != "Calvin"):
      print "That's not my cat!"
    else:
      print "That is my cat!"
  else:
    print "That is my cat!"
else:
  print "That is my cat!"