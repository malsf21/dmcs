import random

iterations = 10000 # how many times you want to run this simulation
people = 23 # how many people are in the room (23 for ~ 50%, 70 for ~99.9%)
days = 365 # how many days are in a year (you can change this to accomodate for whatever calendar system you use)
correct = 0

print " "
print "Generating " + str(iterations) + " sets of data..."

for i in range(iterations):
    found = False
    room = []
    for j in range(people):
        room.append(random.randint(1,days))
    for k in range(len(room)):
        if (found == True):
            break
        else:
            for l in range(1,len(room)-k):
                if (found == True):
                    break
                else:
                    if(room[k] == room[k+l]):
                        correct += 1
                        found = True
print " "
print "Analyzing Data..."
print " "
print str(iterations) + " sets of data were generated."
print " "
print "Two people in the room shared the same birthday " + str(correct) + " times."
print " "
print "There was a " + str(float(correct)/iterations*100) + " percent chance that two people in the room shared the same birthday."
