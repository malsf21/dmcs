ang1 = input("Angle 1")
ang2 = input("Angle 2")
ang3 = input("Angle 3")

if total ang1 + ang2 + ang3 != 180:
	print("Error")
elif ang1 == ang2 and ang2 == ang3:
	print("Equilateral")
elif ang1 == ang2 or  ang2 == ang3:
	print("Scalene")
else:
	print("Isoceles")