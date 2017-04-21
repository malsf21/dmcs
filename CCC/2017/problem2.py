n = long(raw_input(""))
tides = raw_input("").split(" ")
answer = ""

tides = sorted(tides, key=int)
if (n%2 == 1):
    htides = tides[n/2+1:n]
    ltides = tides[0:n/2+1]
else:
    htides = tides[n/2:n]
    ltides = tides[0:n/2]
ltides = ltides[::-1]
for i in range((n/2)):
    answer += ltides[i] + " " + htides[i] + " "
if (n%2 == 1):
    answer += ltides[n/2]

print answer.rstrip()
