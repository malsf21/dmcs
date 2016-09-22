'''
Woohoo! Final Exam! (by Matthew Wang)
This program takes a String input, checks against a "data.txt", 
and finds a player that matches that String input. 
Then, it prints that player's points per game.
'''
#compare function
def compare(filename, istring):
	fileObj = open(filename) #opening file
	for line in fileObj:
		if line.startswith(istring): #checks for first string of player name
			global player
			player = line.split(",")
			fileObj.close() #don't forget to do this!
			return True
	fileObj.close() #don't forget to do this!
	return False


#input
uinput = raw_input("Enter the name of a famous hockey player!")
#checking compares
if compare("data.txt", uinput) == False:
	print "Sorry! Your player isn't in the Top 10." #if compare doesnt return a player
else:
	'''for i in range(7):
		print player[i] 
		#for testing purposes
		'''
		#calculations/out put
	print ("You chose " + player[0] + "! His total points per game is "+ str((float(player[5])+float(player[6]))/float(player[4])))
	print ("Thanks for using this program!") #fun stuff
