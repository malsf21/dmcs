#########################################
# Quadratic Buster, by Matt Wang (2015) #
#                                       #
# The goal of this program was to solve #
# Quadratic Equations without throwing  #
# 500 error messages. Hope it works!    #
#########################################
import math
#handy code to deal with inputs that aren't numbers
def numcheck(num):
	try:
		float(num)
		return True
	except ValueError:
		return False
#checks for how many roots an equation will have by checking the state of the discriminate
def roots(A,B,C):
	discriminate = B*B - 4*A*C
	if discriminate > 0:
		return 2
	elif discriminate == 0:
		return 1
	else:
		return 0
#the actual calculator
def quadratic(A,B,C,roots):
	global root1
	global root2
	root1 = (-B + math.sqrt(B*B - 4*A*C))/2*A
	#check step so it doesnt print the root twice if there's only one root
	if roots == 2: 
		root2 = (-B - math.sqrt(B*B - 4*A*C))/2*A
	else:
		return
#says all func are loaded
print "Quadratics Module Loaded."
#mainloop
while True:
	#user input and stuff. uses loop incase failed attempts
	passed = False
	while passed == False:
		aanswer = raw_input("A: ")
		banswer = raw_input("B: ")
		canswer = raw_input("C: ")
		#makes sure that we dont get a fucked up "number"
		if numcheck (aanswer) == True and numcheck (banswer) == True and numcheck (canswer) == True:
			aanswer = float(aanswer)
			banswer = float(banswer)
			canswer = float(canswer)
			passed = True
		else: 
			print ("Hey, try again. You entered some... wrong inputs. The roots need to be numbers!")

	#output, several conditionals checking for how many roots it needs to print.
	if roots(aanswer,banswer,canswer) == 2:
		quadratic(aanswer,banswer,canswer,2)
		print ("There are two roots.")
		print ("The first root is: " + str(root1))
		print ("The second root is: " + str(root2))
	elif roots(aanswer,banswer,canswer) == 1:
		quadratic(aanswer,banswer,canswer,1)
		print ("There is only one root.")
		print ("The root is: " + str(root1))
	else:
		print ("There are no roots.")
	#checks for endclause
	endclause = raw_input("Hope that helped! If you want to exit, type in \"esc\". Other inputs will start the program again.")
	if endclause == ("esc"):
		break
	else:
		print("Restarting ...")
