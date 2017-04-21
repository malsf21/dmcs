n = int(raw_input(""))
swifts = raw_input("").split(" ")
sem = raw_input("").split(" ")

gw = 0
gs = 0
done = 0

for i in range(n):
    gw += int(swifts[i])
    gs += int(sem[i])
    if (gw == gs):
        done = i+1
print done
