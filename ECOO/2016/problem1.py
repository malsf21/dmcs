file = open("DATA11.txt","r")
for num in range(10):
    weight = file.readline().split(" ")
    for j in range(len(weight)):
        weight[j] = int(weight[j])

    numStudents = int(file.readline())
    passed = 0

    for i in range(numStudents):
        score = file.readline().split(" ")
        for j in range(len(score)):
            score[j] = int(score[j])

        if score[0]*weight[0] + score[1]*weight[1] + score[2]*weight[2] + score[3]*weight[3] >= 5000:
            passed += 1

    print passed

file.close()
