import math
def dist(x,y,ox,oy):
    xdist = abs(x-ox)
    ydist = abs(y-oy)
    distance = float(math.sqrt(xdist**2+ydist**2))
    if distance <= 50:
        return distance
    else:
        return False

lattice = []
for i in range(102):
    for j in range(102):
        element = [i-51,j-51]
        if dist(i-51,j-51,0,0) != False:
            lattice.append(list(element))

# for i in range(102):
#     row = []
#     row.append(i-51)
#     for j in range(102):
#         for k in range(len(row)):
#             row[k] = [row[k], j-51]
#         lattice.append(list(row))

print lattice
