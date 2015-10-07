fileIn = open("words.txt", "r")
fileOut = open("words_longest.txt", "w")
longword = "a"
longwordc = 1

for word in fileIn:
	if len(word) > longwordc:
		longwordc = len(word)
fileIn.close()

fileIn = open("words.txt", "r")

for word in fileIn:
	if len(word) == longwordc:
		fileOut.write(word)
fileIn.close()
fileOut.close()
