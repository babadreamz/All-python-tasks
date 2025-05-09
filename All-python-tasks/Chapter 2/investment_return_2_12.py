p = 1000
r = 0.07
number = [10, 20, 30]

for number_of_years in range(3):
	amount = p * (1 + r)**number[number_of_years]
	print(f"amount on deposit after {number[number_of_years]} years is {amount:.2f}")