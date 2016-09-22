#########################################
#  Factor finder, by Matt Wang (2015)   #
#                                       #
# The goal of this program was to find  #
# how many factors a number has without #
# 500 error messages. Hope it works!    #
#########################################
#code that checks whether or not something is a number
def numcheck(num):
	try:
		float(num)
		return True
	except ValueError:
		return False
#code that checks whether or not a number is prime
def checkprime (num):
	for i in range(num):
		if num % (i+2) == 0 and num != i+2:
			return False
	return True
#code that checks how many factors a number has/appends it to a list
def numfactor(num):
	for i in range(num):
		if num % (i+1) == 0:
			factors.append(i+1)
#declares a factors list just because im shitty at code
factors = []
#each of these things just prints out a new line to keep the terminal output clean
print("   ")
#while loop that runs the main program
while True:
	inp = raw_input("Please enter a positive integer (we'll truncate the number).")
	print("   ")
	#first checks if the input is an actual number
	if numcheck(inp) == False:
		print("   ")
		#the end clause basically just checks an input on whether or not somebody feels like exiting the program
		endclause = raw_input("Welp you entered a wrong type of input! If you want to exit, type in \"esc\". Other inputs will start the program again. ")
	#next it checks whether or not the number is 0, because that's a special case
	elif int(inp) == 0:
		print ("0 is a special little snowflake! It technically doesn't have any factors!")
		print("   ")
		endclause = raw_input("Awesome, if you want to exit, type in \"esc\". Other inputs will start the program again. ")
	#also checks for 1, because that's a special case
	elif int(inp) == 1:
		print ("1 isn't prime or composite, it's special. 1 has only one factor, 1.")
		print("   ")
		endclause = raw_input("Awesome, if you want to exit, type in \"esc\". Other inputs will start the program again. ")
	#if not, we can do something for all integers equal to and above 2, which should be either composite and prime and has 2+ factors
	elif int(inp) >= 2:
		#if the number isn't prime, it's composite
		if checkprime(int(inp)) == False:
			print inp + " is composite! It's factors are: "
			numfactor(int(inp))
			#prints out all the factors line by line
			for num in factors:
				print num
		#prime numbers only have two factors, itself and 1
		else:
			print (inp + " is prime! It has two factors, 1 and " + inp + " .")
		print("   ")
		endclause = raw_input("Awesome, if you want to exit, type in \"esc\". Other inputs will start the program again. ")
	#finally, if its not 0, 1, or 2+, the its negative. we can't find factors for negative numbers, or at least not technically
	else:
		print ("Unfortunately, it's pretty hard to find factors for negative numbers. ")
		print("   ")
		endclause = raw_input("Welp, if you want to exit, type in \"esc\". Other inputs will start the program again. ")
	#checks if user wants to back out; breaks if they do, and restarts the loop if it doesn't
	if endclause == ("esc"):
		break
	else:
		print("   ")
		print("Restarting ...")
		print("   ")
