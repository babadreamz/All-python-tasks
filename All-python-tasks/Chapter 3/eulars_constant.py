import math
denominator = 0
term = 0
total = 0

for count in range (0, 11):
	term = 1 / math.factorial(denominator)
	total += term
	denominator += 1
	
print(f"The value of constant e after summing 10 times is {total}")