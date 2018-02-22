nvillages = int(raw_input(""))
villages = []
for i in range(nvillages):
    temp = float(raw_input(""))
    villages.append(temp)
villages = sorted(villages)
smallest = 1000000000
for i in range(nvillages-2):
    dist = abs(villages[i+1]-villages[i])/2 + abs(villages[i+2]-villages[i+1])/2
    if dist < smallest:
        smallest = dist
print round(smallest,1)
