import csv
import random

print " "
iterations = input("How many times do you want to run this game? ");
types = [0,0,0,0]
answers = []
doors = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [2, 0, 1],
    [1, 2, 0],
    [2, 1, 0]
]

for i in range(iterations):
    won = False
    setup = random.choice(doors)
    print " "
    print "Welcome to the Monty Hall gameshow. You're here to win a brand-spanking-new Bugatti Veyron."
    print " "
    print "There are three doors in front of you. 2 of them contain Speeding Bullet 2 Heaven by Kid Cudi. The other contains the Bugatti Veyron."
    print " "
    uinput1 = input("Pick a door! (type in 1, 2, or 3) ")
    uinput1 = int(uinput1)
    while True:
        chosen = random.choice([1,2,3])
        if setup[chosen-1] != 0 and chosen != uinput1:
            break
    print " "
    print "Surprise! Door " + str(int(chosen)) + " contains Speeding Bullet 2 Heaven by Kid Cudi. Now, you have two options: the door you chose, or the other door over there."
    print " "
    uinput2 = raw_input("Do you switch? (type in \"y\" to switch, \"n\" to not.) ")
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
    print " "
    if won:
        print "Congrats, you won! Let's go for another try!"
    else:
        print "You lost. Try again next time!"
    answers.append([uinput2, won])
print " "
print "Printing Answers..."
with open('answers.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(answers)):
        print answers[i]
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
print "The player had a " + str(float(types[2])/(types[2]+types[3]))*100) + " percent chance of winning when they switched, and a " + str(float(types[0])/(types[0]+types[1])*100) + " percent chance of winning when they didn't."
