principal = int(input("Enter the principal: "))

rate = int(input("Enter the rate: "))
rate_percent = rate / 100

for years in range (1,31):
	noOfYears = int(input(f"Enter the years {years}: "))
	
	amount = principal * (1 + rate)**noOfYears

	print("The amount of money you get each year %2d " %amount)
