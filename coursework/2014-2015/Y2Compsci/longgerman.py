#file io
filei = open("german.txt", "r")
fileo = open("german_longest.txt", "w")

#declare var
longw = "a"
longn = 1

#main

for word in filei:
	if len(word) > longn:
		longn = len(word)
filei.close()
filei = open("german.txt", "r")

for word in filei:
	if len(word) == longn:
		fileo.write(word)
filei.close()
fileo.close()
