fileObj = open("words.txt")
for word in fileObj:
	if word.startswith("x") == True :
		print word.capitalize()
fileObj.close()
