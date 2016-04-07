#07:00-10:00, 15:00-19:00
departure = raw_input("")
depsplit = departure.split(":")
time = int(depsplit[0])*60 + int(depsplit[1])
distcounter = 0
while distcounter < 24:
    if time >= 7 * 60 and time < 10 * 60:
        distcounter += 1
    elif time >= 15*60 and time < 19*60:
        distcounter += 1
    else:
        distcounter += 2
    time += 10
timeh = (time)/60
timem = (time)%60
if timem >= 60:
    timeh += 1
    timem = timem - 60
if timeh >= 24:
    timeh = timeh % 24
if timeh < 10:
    if timem == 0:
        output = "0" + str(timeh) + ":" + "00"
    else:
        output = "0" + str(timeh) + ":" + str(timem)
else:
    if timem == 0:
        output = str(timeh) + ":" + "00"
    else:
        output = str(timeh) + ":" + str(timem)
print output
