success = False
for i in range(0,3):
  if success == False:      #Has the user succeeded yet?
    name = raw_input("Please choose a cat name:\n")
    if (name != "Captain Haddock") and (name != "Calvin"):
      print "That's not my cat!"
    else:
      print "That is my cat!"
      success = True        #Set the value of success to True since the user has guessed correctly