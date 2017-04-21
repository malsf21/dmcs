n = int(raw_input(""))
boards = raw_input("").split(" ")
adds = []
lc = 0
if (n==2):
    print "1 1"
else:
    longest = int(boards[0])+int(boards[n/2])
    for i in range(n/2):
        for j in range((n-i+1)/2):
            temp = int(boards[i])+int(boards[n-j-1])
            if (temp >= longest):
                if (temp in adds):
                    if (temp > longest):
                        longest = temp
                        lc = 2
                    else:
                        lc += 1
                adds.append(temp)
                # print longest
                # print lc
    if lc == 0:
        print "1 " + str((n-1)*n/2)
    else:
        print str(lc) + " " + str(1)
