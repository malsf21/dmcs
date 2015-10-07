votes = raw_input("Should Scotland separate? Enter Y or N consecutively : ")
yes = 0
no = 0

for vote in votes:
		if vote == "y":
			yes = yes + 1
		else:
			no = no + 1
print("Separation Votes " + str(yes))
print("Non-separation Votes " + stry(no))
if yes > no:
	print("Scotland is free! Wins by " + str(yes-no))
elif no > yes:
	print("Scotland is stuck with Britain until the next referendum " + str(no-yes))
else:
	print("Tie, I guess Scotland is stuck with Britain again!")