n = int(raw_input(""))
orgarr = []
for i in range(n):
    temp = map(int, raw_input("").split(" "))
    orgarr.append(temp)

horarr = []
verarr = []

for i in range(n):
    horarr.append(sum(orgarr[i]))
for i in range(n):
    verarr.append(0)
    for j in range(n):
        verarr[i] += orgarr[j][i]

if (sorted(horarr) == horarr):
    vert = True
else:
    vert = False

if (sorted(verarr) == verarr):
    horz = True
else:
    horz = False

if (horz == True):
    if (vert == True):
        for i in range(n):
            pline = ""
            for j in range(n):
                pline += str(orgarr[i][j]) + " "
            print pline[:-1]
    else:
        for i in range(n):
            pline = ""
            for j in range(n):
                pline += str(orgarr[n-j-1][i]) + " "
            print pline[:-1]
else:
    if (vert == True):
        for i in range(n):
            pline = ""
            for j in range(n):
                pline += str(orgarr[j][n-i-1]) + " "
            print pline[:-1]
    else:
        for i in range(n):
            pline = ""
            for j in range(n):
                pline += str(orgarr[n-i-1][n-j-1]) + " "
            print pline[:-1]
