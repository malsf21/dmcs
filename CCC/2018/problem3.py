fline = raw_input("").split(" ")
n = int(fline[0])
m = int(fline[1])
map = []
spos = []
for i in range(n):
    temp = list(raw_input(""))
    if "S" in temp:
        spos = [i,temp.index("S")]
    map.append(temp)

def next_path(curry, currx):
    nanswer = []
    if (map[curry][currx-1] == "."):
        if (is_caught(curry,currx-1) == False):
            nanswer.append([curry,currx-1])
    if (map[curry][currx+1] == "."):
        if (is_caught(curry,currx+1) == False):
            nanswer.append([curry,currx+1])
    if (map[curry-1][currx] == "."):
        if (is_caught(curry-1,currx) == False):
            nanswer.append([curry-1,currx])
    if (map[curry+1][currx] == "."):
        if (is_caught(curry+1,currx) == False):
            nanswer.append([curry+1,currx])
    return nanswer

def is_caught(curry,currx):
    if (map[curry][currx-1] == "C"):
        return True
    if (map[curry][currx+1] == "C"):
        return True
    if (map[curry-1][currx] == "C"):
        return True
    if (map[curry+1][currx] == "C"):
        return True
    return False

def is_path(starty, startx, finaly, finalx, count, path):
    count += 1
    path.append([starty,startx])
    print [starty, startx, finaly, finalx, count, path]
    temp = next_path(starty, startx)
    if len(temp) == 0:
        panswer.append(-1)
        return
    tempf = list(temp)
    for k in range(len(temp)):
        if temp[k] in path:
            tempf.remove(temp[k])
    print tempf
    if (len(tempf)>0):
        for k in range(len(tempf)):
            if tempf[k] == [finaly, finalx]:
                print "FOUND! " + str(tempf[k][0]) + str(tempf[k][1]) + " TOOK " + str(count)
                path = [spos[0],spos[1]]
                panswer.append(count)
                return
            else:
                is_path(tempf[k][0],tempf[k][1], finaly, finalx, count, path)
    else:
        panswer.append(-1)

fanswer = []
tcount = 0
for i in range(n-2):
    for j in range(m-2):
        if map[i+1][j+1] == ".":
            tcount += 1
            print "Count: " + str(tcount)
            panswer = []
            r = is_path(spos[0],spos[1], i+1, j+1, 0, [])
            print panswer
            tempanswer = sorted([value for value in panswer if value != -1])
            if len(tempanswer) == 0:
                fanswer.append(-1)
            else:
                fanswer.append(tempanswer[0])
for i in range(len(fanswer)):
    print fanswer[i]
