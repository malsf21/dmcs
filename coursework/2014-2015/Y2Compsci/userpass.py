attempts = 0
user = "name"
pw = "word"

while attempts < 3:
	nuser = raw_input("Identify yourself!")
	npw = raw_input("What is the magic word?")
	if user == nuser and pw == npw:
		print("Welcome to paradise!")
		attempts = 99
	else:
		attempts += 1
		print("You. Shall. Not. Pass. " + 3-attempts + " attempts remaining")
