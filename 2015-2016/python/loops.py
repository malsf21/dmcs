import sys

all_data = sys.stdin.read().split('\n')

trout = int(all_data[0])
pike = int(all_data[1])
pickerel = int(all_data[2])
old_total = int(all_data[3])

# trout = int(input("Trout points ")) #user input of # of points 1 trout is worth
# pike = int(input("pike points ")) #user input of # of points 1 pike is worth
# pickerel = int(input("pickerel points ")) #user input of # of points 1 pickerel is worth
# old_total = int(input("total points ")) #user input of maximum # of points a fish can add up to

#declaring variables (instantiating)
trouts = []
pikes = []
pickerels = []

#logic loops
for i in range (0, old_total+1): #for loop counter called i, that represents the # of trouts. runs for the amount of times that are possible for trouts: it ranges from 0 (the minimum # of trouts), to the old_total (the maximum amount (the + 1 is to offset range inclusion))

	for j in range (0, old_total+1): #ditto as above; except for pike and j; NESTED LOOPS!!!!

		for k in range (0, old_total+1):  #ditto as above; except for pickerel and k

			if i*trout + j*pike + k*pickerel <= old_total: #checks whether or not number of fish * points per fish for each type of fish adds up; or, do our values for the # of fish solve our problem?

				if i > 0 or j > 0 or k > 0: #nested conditional to check if the total # of fish is > 1 ; if not, the code inside won't run

					# debugging
					# print i
					# print j
					# print k

					#if the solution is correct, we add our current set of values to our respective arrays
					trouts.append(i)
					pikes.append(j)
					pickerels.append(k)


for a in range (0, len(trouts)): #for loop that runs for the length of our array; or our number of solutions

	print (str(trouts[a]) + " Brown Trout, " + str(pikes[a]) + " Northern Pike, " + str(pickerels[a]) + " Yellow Pickerel")
	#prints the value for each time; references the index of the array for the correct value

print ("Number of ways to catch fish: " + str(len(trouts))) #prints out number of ways

