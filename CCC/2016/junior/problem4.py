#07:00-10:00, 15:00-19:00
departure = raw_input("")
depsplit = departure.split(":")
time = int(depsplit[0])*60 + int(depsplit[1])
if time <= 5*60:
    output = "0" + str(int(depsplit[0])+2) + ":" + depsplit[1]
elif time >= 19*60:
    if int(depsplit[0])+2 >= 24:
        output = "0" + str((int(depsplit[0])+2)%24) + ":" + depsplit[1]
    else:
        output = str(int(depsplit[0])+2) + ":" + depsplit[1]
elif time >= 10*60 and time <= 13*60:
    output = str(int(depsplit[0])+2) + ":" + depsplit[1]
elif time < 10*60:
    if time <= 7*60:
        timeout = 7*60-time
        timein = 2*(120-timeout)
        if timein > 180:
            timeout += (timein-180)/2
            timein = 180
    else:
        timein = 10*60-time
        timeout = 120 - timein/2
    timeh = (timein + timeout)/60
    timem = (timein + timeout)%60
    newtimeh = int(depsplit[0])+timeh
    newtimem = int(depsplit[1])+timem
    if newtimem >= 60:
        newtimem = newtimem - 60
        newtimeh += 1
    if newtimem == 0:
        if int(depsplit[0])+timeh < 10:
            output = "0" + str(newtimeh) + ":" + "00"
        else:
            output = str(newtimeh) + ":" + "00"
    else:
        if int(depsplit[0])+timeh < 10:
            output = "0" + str(newtimeh) + ":" + str(newtimem)
        else:
            output = str(newtimeh) + ":" + str(newtimem)
else:
    if time <= 15*60:
        timeout = 15*60-time
        timein = 2*(120-timeout)
        if timein > 240:
            timeout += (timein-240)/2
            timein = 240
    else:
        timein = 19*60-time
        timeout = 120 - timein/2
    timeh = (timein + timeout)/60
    timem = (timein + timeout)%60
    newtimeh = int(depsplit[0])+timeh
    newtimem = int(depsplit[1])+timem
    if newtimem >= 60:
        newtimem = newtimem - 60
        newtimeh += 1
    if newtimem == 0:
        output = str(newtimeh) + ":" + "00"
    else:
        output = str(newtimeh) + ":" + str(newtimem)
#
print output
