secretnum = 42
count = 0

while count < 4:
	num = input("What is the answer to life, the universe, and everything?")
	if num == secretnum:
		print("Correct! Please collect your towel at the front door.")
		count = 5
	elif count == 3:
		print("That was the last straw. So long, and thanks for all the fish.")
	else:
		if num > secretnum:
			print("Your number is like the IQ of dolphins; too high.")
		else:
			print("Your number is like the IQ of humans; too low and worthless.")
		count = count + 1