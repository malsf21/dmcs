departure = raw_input("")
depsplit = departure.split(":")
time = int(depsplit[0])*60 + int(depsplit[1])
if time <= 5*60:
    output = "0" + str(int(depsplit[0])+2) + ":" + depsplit[1]
elif time >= 19*60:
    if int(depsplit[0])+2 >= 24:
        output = "0" + str((int(depsplit[0])+2)%12) + ":" + depsplit[1]
    else:
        output = str(int(depsplit[0])+2) + ":" + depsplit[1]
elif time >= 10*60 and time <= 13*60:
    output = str(int(depsplit[0])+2) + ":" + depsplit[1]
elif time < 10*60:
    timein = 10*60-time
    timeout = 120 - timein/2
    timeh = (timein + timeout)/60
    timem = (timein + timeout)%60
    output = str(int(depsplit[0])+timeh) + ":" + str(int(depsplit[1])+timem)
else:
    timein = 19*60-time
    timeout = 120 - timein/2
    timeh = (timein + timeout)/60
    timem = (timein + timeout)%60
    output = str(int(depsplit[0])+timeh) + ":" + str(int(depsplit[1])+timem)
print output
