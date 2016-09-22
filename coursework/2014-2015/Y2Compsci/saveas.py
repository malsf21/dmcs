''' no flex zone - watsky & Karmin
matthew wang - jan 22 2015
saveas.py file i/o functionality, adds line # to new format
'''

#open poem, r parameter for read only
filein = open("poem.txt","r")
#new file, use w parameter, w mode means write or overwrite existing
fileout = open("poem_new.txt", "w")

count = 1
for line in filein:
	fileout.write("Line " + str(count) + ": " + line)
	count = count + 1

filein.close()
fileout.close()