with open("DATA32.txt", "r") as data:
     data = data.readlines()

for i in range(10):
    a = int(data.pop(0))
    train = data.pop(0).strip().split(" ")
    for i in range(len(train)):
        train[i] = int(train[i])

    while True:
        if a == 1:
            break
        if train.index(a) > train.index(a-1):
            a -= 1
        else:
            a -= 1
            break

    if a == 1:
        print 0
        continue

    count = 0
    while train != sorted and a > 0:
        pos = train.index(a)
        train.pop(pos)
        count += pos
        train = [a] + train
        a -= 1

    print count
