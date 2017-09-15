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