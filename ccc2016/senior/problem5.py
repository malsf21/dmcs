numN = raw_input("").split(" ")
beginStep = raw_input("")
thisStep = beginStep
for i in range(1,long(numN[1])+1):
    nextStep = []

    alives = 0
    if long(thisStep[len(thisStep)-1]) == 1:
        alives += 1
    if long(thisStep[1]) == 1:
        alives += 1
    if alives == 1:
        nextStep.append("1")
    else:
        nextStep.append("0")

    for i in range(1,long(numN[0])-1):
        alives = 0
        if long(thisStep[i-1]) == 1:
            alives += 1
            #print "To the left of " + str(i) + " is a 1"
        if long(thisStep[i+1]) == 1:
            alives += 1
            #print "To the right of " + str(i) + " is a 1"
        if alives == 1:
            nextStep.append("1")
        else:
            nextStep.append("0")

    alives = 0
    if long(thisStep[len(thisStep)-2]) == 1:
        alives += 1
    if long(thisStep[0]) == 1:
        alives += 1
    if alives == 1:
        nextStep.append("1")
    else:
        nextStep.append("0")
    thisStep = nextStep
print ''.join(nextStep)
