qtype = input("")
cit = input("")
dmo = raw_input("").split(" ")
peg = raw_input("").split(" ")
totalspeed = 0
totalspeed1 = 0
totalspeed2 = 0
dmosort = sorted(dmo, key = int)
pegsort = sorted(peg, key = int)
if qtype == 1:
    for i in range(cit):
        totalspeed += max(int(dmosort[i-1]), int(pegsort[i-1]))
else:
    for i in range(cit):
        totalspeed += max(int(dmosort[::-1][i-1]), int(pegsort[i-1]))
print totalspeed
