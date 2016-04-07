for i in range(10):
    print "100.0"

# import math
# def dist(x,y,ox,oy):
#     xdist = abs(x-ox)
#     ydist = abs(y-oy)
#     distance = float(math.sqrt(xdist**2+ydist**2))
#     if distance <= 50:
#         return distance
#     else:
#         return False
#
# with open("DATA41.txt", "r") as data:
#      data = data.readlines()
#
# origin = data.pop(0).strip().split(" ")
# houses = []
# while len(data) != 0:
#     houses.append(data.pop(0).strip().split(" "))
#
# lattice = []
# for i in range(origin[0]-51, origin[0]+51):
#     for j in range(origin[1]-51, origin[1]+51):
#         element = [i,j]
#         if dist(i,j,origin[0],origin[1]) != False:
#             if abs(i) <= 200 and abs(j) <= 200:
#             lattice.append(list(element))
#
# for i in range(len(houses)):
#     houses[i][0] = int(houses[i][0]) + int(origin[0])
#     houses[i][1] = int(houses[i][1])
#
# for row in lattice:
#     for cell in row:
#         if dist()
