import csv
import random

iterations = 1000000 # how many times you want to run this! change if needed.
answers = []
types = [0,0,0,0]
doors = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [2, 0, 1],
    [1, 2, 0],
    [2, 1, 0]
]
print " "
print "Generating " + str(iterations) + " sets of data..."
for i in range(iterations):
    won = False
    setup = random.choice(doors)
    uinput1 = random.choice([1,2,3])
    while True:
        chosen = random.choice([1,2,3])
        if setup[chosen-1] != 0 and chosen != uinput1:
            break
    uinput2 = random.choice(["y", "n"])
    if uinput2 == "n":
        if setup[uinput1-1] == 0:
            won = True
            types[0] += 1
        else:
            types[1] += 1
    else:
        if setup[uinput1-1] != 0:
            won = True
            types[2] += 1
        else:
            types[3] += 1
    answers.append([uinput2, won])
print " "
print "Printing Answers..."
with open('answers.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(answers)):
        writer.writerow(answers[i][0])
print " "
print "Analyzing Data..."
print " "
print "The player lost " + str(types[1] + types[3]) + " times."
print " "
print "The player won " + str(types[0]) + " times when they didn't switch."
print " "
print "The player won " + str(types[2]) + " times when they switched."
print " "
print "The player had a " + str(float(types[2])/(types[2]+types[3])*100) + " percent chance of winning when they switched, and a " + str(float(types[0])/(types[0]+types[1])*100) + " percent chance of winning when they didn't."
