import random

iterations = 1000
boxes = 100
correct = 0
numbers = []

for i in range(boxes):
    numbers.append(i)

print " "
print "Generating " + str(iterations) + " sets of data..."

for j in range(iterations):
    currentFound = 0
    setboxes = numbers
    random.shuffle(setboxes)
    for i in range(boxes):
        solved = "false"
        counter = 0
        while solved == "false":
            if (counter >= (boxes/2)):
                solved = "failed"
            elif int(setboxes[counter]) == i:
                solved = "true"
                currentFound += 1
            else:
                counter += 1
    if (currentFound == boxes):
        correct += 1
print " "
print "Analyzing Data..."
print " "
print "Every prisoner found their card " + str(float(correct*100)/(iterations)) + " percent of the time."
