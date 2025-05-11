principal = int(input("Enter the principal: "))

interest = int(input("Enter the interest: "))
interest_percent = interest/100

for no_of_years in range (1,31):
	duration= int(input("Enter the duration : "))
	
	amount = principal * (1 + interest_percent)**duration

	print(f"The amount of money you get at the end of year {duration} is ${amount:.2f}")

