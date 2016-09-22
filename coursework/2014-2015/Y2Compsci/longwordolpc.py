''' 
Matt Wang's longword finder. finds longest words, + ties, in file words.txt. 
outputs to words_longest.txt
made january 28th 2014
'''


fileIn = open("words.txt", "r") #opening stuff
fileOut = open("words_longest.txt", "w") #opening more stuff
#setting vars
longword = "a"
longwordc = 1

for word in fileIn: #for loop that decides what the longest word count is
	if len(word) > longwordc:
		longwordc = len(word)#finds longest number of letters in longest word
#close + reopen to start as front again
fileIn.close()

fileIn = open("words.txt", "r")

for word in fileIn: #finds every instance of longest word per character
	if len(word) == longwordc:
		fileOut.write(word)#outputs longest ones to file
#closes everything
fileIn.close()
fileOut.close()
