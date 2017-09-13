
mycats = ["Calvin","Captain Haddock"] #If we define our list here, it's easy to change later
me = "Carolyn"

def isitmycat(guess,cats): 	#We name the arguments to the function in the parentheses
	if guess in cats:
		print "That's my cat!"
	else:
		print "That's not my cat."

def isitme(guess,name): 	#We name the arguments to the function in the parentheses
	if guess == name:
		print "That's me!"
	else:
		print "That's not me."

print "Welcome!"

quit = False				#Initialize quit to False
while quit == False:		#Stop when isitmycat() returns True
	print "Please pick an option: "
	print "1. Play is-it-my-cat"
	print "2. Play is-it-me"
	print "3. Quit"
	choice = int(raw_input("Your choice is: "))
	if choice == 3:
		print "Thanks for playing!"
		quit = True
	else:
		guess = raw_input("Your guess is: ")
		if choice == 1:
			isitmycat(guess,mycats)
		else:
			isitme(guess,me)