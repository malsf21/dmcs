inputnum = 28312893
new_num = inputnum

def isPrime(number):
	if number < 2:
		return False
	else:
		for i in range(2,number): 
			if number % i == 0:
				return False
				break
		return True

while isPrime(new_num) == False:
	new_num += 1

print new_num


