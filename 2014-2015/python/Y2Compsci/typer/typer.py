'''
Matthew Wang's typer pro (tm).
Sources: StackOverflow, Python Documentation
Has algorithm to determine imported dictionary,
 quizzes users on different difficulties, and includes a timer and goldstar system.
'''
#importing libraries
from random import randint
import time
import os
import welcome

#defining all my variables
dicta = []
fword = ""
iword = ""
utime = 0
diff = 0.0
dictt = 0


#clearscreen function
def cls():
	os.system(['clear','cls'][os.name == 'nt'])

#dictimport function; imports the provided dictionary
def dictimport():
	global dictt
	print("Importing dictionary, please wait!")
	finput = open("words.txt", "r")
	for word in finput:
		dicta.append(word)
		dictt = dictt + 1
	print("Dictionary imported!")
	finput.close()

#goldstar retrieval, for user goldstarring
def gretrieve():
	global goldstar
	ginput = open("goldstar.txt", "r")
	for line in ginput:
		goldstar = int(line)
	ginput.close()
	print("Gold stars loaded!")

#goldstar storing, for user goldstarring
def gplace():
	ginput = open("goldstar.txt", "w")
	ginput.write(str(goldstar))
	ginput.close()
	print("Gold stars stored!")

#make word and difficulty using an algorithm based on the word
def mword(diffr):
	global fword
	global diff
	fword = dicta[randint(0,dictt-1)]
	while len(fword)> diffr+3 or len(fword) < diffr-1 :
		fword = dicta[randint(0,dictt-1)]
	diff = len(fword)*3/(diffr*2)

#main typer engine, does the counting with the timer and the main text/user response of the code
def typep():
	atry = False
	global iword
	stime = time.time()
	iword = raw_input("Please type out this word correctly: " + fword)
	while atry == False: #loop to check for time
		if len(iword) > 0:
			if fword.rstrip() == iword:
				ctime = time.time()
				if stime + diff >= ctime:#success checker
					atry = True
					print("Nice job! You did it ! Have a Gold Star!")
					global goldstar
					goldstar = goldstar + 1
				else: #failed by time
					atry = True
					print("Nice try! Unforunately, you timed out. Though, typing " + fword.rstrip() + " is hard.")
					print("Better luck next time!")
			else: #failed by misspell
					atry = True
					print("Nice try! Unforunately, you failed. Though, typing " + fword.rstrip() + " is hard.")
					print("Better luck next time!")
	time.sleep(2)
	cls()

#startup function with loading, waits, clears, rights, and loops
def startup():
	time.sleep(0.25)
	cls()
	print("loading")
	time.sleep(0.25)
	cls()
	print("loading.")
	time.sleep(0.25)
	cls()
	print("loading..")
	time.sleep(0.25)
	cls()
	print("loading...")
	time.sleep(0.25)
	cls()


#gamemenu chooser, just a bunch of statements based on choices
def gamemenu():
	cls()
	quita = False
	time.sleep(0.5)
	print("Welcome to Typer Pro (Lite)! Typer Pro tests your typing skills from your imported dictionary!")
	while quita == False: #quit loop
		print("Hello!")
		print("In order to start playing, type in your difficulty from 1-10")
		print("To access your goldstar count, type in 11")
		print("In order to exit, type in 404")
		uinput = input()
		#logic for choosing
		if uinput == 404:
			cls()
			quita = True
		elif uinput > 0 and uinput < 11:
			mword(uinput)
			typep()
			print("Returning to game menu! Please wait!")
			time.sleep(1.5)
			cls()
		elif uinput == 11:
			print(str(goldstar))
		else:
			print("Seems like you mistyped. We will now restart the program.")
			cls()

#main program run through
dictimport()
gretrieve()
startup()
gamemenu()
gplace()
cls()