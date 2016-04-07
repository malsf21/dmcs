# with open("DATA21.txt", "r") as data:
#     data = data.readlines()
#
# for i in range(0,10):
#     line1 = data.pop(0).strip("")
#     line2 = data.pop(0).strip("")
#     line3 = data.pop(0).strip("")
#
#     s = line2.split(" ")
#     combinations = []
#
#     for i in range(len(s)):
#         s[i] = int(s[i])
#
#
#     for i in s:
#         for j in s:
#             for k in s:
#                 combinations.append(i+j+k)
#                 combinations.append(i*j+k)
#                 combinations.append((i+j)*k)
#                 combinations.append(i*j*k)
#
#     t = line3.split(" ")
#     for i in range(len(t)):
#         t[i] = int(t[i])
#
#     print ""
#     for i in t:
#         if i in combinations:
#             print "\bT",
#         else:
#             print "\bF",

file = open("DATA21.txt", "r")

for i in range (10):
    numSpinChoices = int(file.readline())
    spinChoices = file.readline().split(" ")
    for i in range(numSpinChoices):
        spinChoices[i] = int(spinChoices[i])

    targets = file.readline().split(" ")
    for i in range(len(targets)):
        targets[i] = int(targets[i])

    result = ""

    for target in targets:
        works = False

        # check if all three multiply
        for i in spinChoices:
            if (target % i == 0):
                newTarget = target/i
                for j in spinChoices:
                    if (newTarget % j == 0):
                        if (newTarget/j) in spinChoices:
                            works = True
                            break
                if works:
                    break

        # check if add then multiply
        if not works:
            for i in spinChoices:
                if (target % i == 0):
                    newTarget = target/i
                    for j in spinChoices:
                        if (newTarget - j) in spinChoices:
                            works = True
                            break
                    if works:
                        break

        if not works:
            # check if multiply then add
            for i in spinChoices:
                newTarget = target - i
                for j in spinChoices:
                    if newTarget % j == 0:
                        if (newTarget/j) in spinChoices:
                            works = True
                            break
                if works:
                    break

        if not works:
            # check if add then add
            for i in spinChoices:
                newTarget = target - i
                for j in spinChoices:
                    if (newTarget - j) in spinChoices:
                        works = True
                        break
                if works:
                    break

        if works:
            result += "T"
        else:
            result += "F"

    print result

file.close()
