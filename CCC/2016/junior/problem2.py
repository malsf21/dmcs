def magicSquare():
    line = []
    for i in range(4):
      line.append(raw_input(""))
    line1 = line[0].split(" ")
    line2 = line[1].split(" ")
    line3 = line[2].split(" ")
    line4 = line[3].split(" ")
    sum = []
    for i in range(4):
        sum.append(int(line1[i-1]) + int(line2[i-1]) + int(line3[i-1]) + int(line4[i-1]))
    sum.append(int(line1[0]) + int(line1[1]) + int(line1[2]) + int(line1[3]))
    sum.append(int(line2[0]) + int(line2[1]) + int(line2[2]) + int(line2[3]))
    sum.append(int(line3[0]) + int(line3[1]) + int(line3[2]) + int(line3[3]))
    sum.append(int(line4[0]) + int(line4[1]) + int(line4[2]) + int(line4[3]))
    for i in range(7):
        if sum[i-1] != sum[i]:
            return False
    return True
if magicSquare() == False:
    print "not magic"
else:
    print "magic"
