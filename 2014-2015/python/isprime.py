#########################################
#  Prime Checker, by Matt Wang (2015)   #
#                                       #
# The goal of this program was to find  #
# whether or not a number is prime, not #
# having 500 error messages. ;), Enjoy! #
#########################################
#function that checks if the input is a number
def numcheck (num):
	try:
		int(num)
		return True
	except ValueError:
		return Falseprint("Prime Number checker loaded.")
#function that checks if a number is prime
def checkprime (num):
	for i in range(num):
		if num % (i+2) == 0 and num != i+2:
			return False
	return True
#main loop for the program
while True:
	inp = raw_input("Enter an integer: ")
	#checks if input is a number
	if numcheck(int(inp)) == False:
		endclause = raw_input("Welp you entered a wrong input! If you want to exit, type in \"esc\". Other inputs will start the program again.")
	else:
		# 0 and 1 are special cases, neither prime nor composite
		if int(inp) == 0 or int(inp) == 1:
			print("Ooh, this is a tricky one. " + inp + " isn't prime or composite!")
		#if num aint prime, its composite
		elif checkprime(int(inp)) == False:
			print("Composite")
		#if num is prime, its prime
		else:
			print("Prime")
		#goes through input check if the user wants to quit
		endclause = raw_input("Hope that helped! If you want to exit, type in \"esc\". Other inputs will start the program again.")
	#breaks mainloop if user wants to leave
	if endclause == ("esc"):
		break
	else:
		print("Restarting ...")
