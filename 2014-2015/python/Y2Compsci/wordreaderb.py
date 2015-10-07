fileObj = open("words.txt")
for word in fileObj:
	if word.startswith("z") == True :
		print word.upper()
fileObj.close()
