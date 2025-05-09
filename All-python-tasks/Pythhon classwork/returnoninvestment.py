amount = int(input("Enter your investment amount: "))
number_of_years = int(input("Enter your investment duration: "))
interest = int(input("What is your interest rate: "))
interest_rate = interest/100

for count in range(1,number_of_years + 1):
	roi = amount * interest_rate 
	amount = roi + amount
	print(f"Amount after {count}years is ${amount:.2f}")
