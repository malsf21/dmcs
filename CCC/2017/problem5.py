l1 = raw_input("").split(" ")
n = int(l1[0])
m = int(l1[1])
q = int(l1[2])
sassign = raw_input("").split(" ")
passign = raw_input("").split(" ")
# print passign
lines = []
#print q
for i in range(q):
    temp = raw_input("").split(" ")
    lines.append(temp)
for line in lines:
    if (int(line[0]) == 2):
        # print "Moving for " + str(line[1])
        nassign = list(passign)
        temp1 = -1
        temp2 = 0
        for i in range(n):
            # print "assigning for " + str(i)
            # print passign[i]
            if (int(sassign[i]) == int(line[1])):
                # print "match"
                if (temp1 == -1):
                    temp1 = i
                    temp2 = passign[i]
                else:
                    nassign[i] = int(temp2)
                    temp2 = passign[i]
            # print nassign
        nassign[temp1] = int(temp2)
        passign = list(nassign)
        # print passign
        # print "Move done"
    else:
        # print "Surveying for " + line[1] + " " + line[2]
        temp1 = 0
        for i in range(int(line[2])-int(line[1])+1):
            temp1 += int(passign[int(line[1])+i-1])
        print temp1
        # print "Survey Done"
