purchase_price = float(input("Enter purchase price: "))
if purchase_price > 1.00 or purchase_price < 0:
	print("Invalid Price");
else : 
	change = round((1.00 - purchase_price) * 100)
	
	quarters = change // 25
	change %= 25

	dimes = change // 10
	change %= 10

	nickels = change // 5
	change %= 5

	pennies = change
	
	print("Your change is: ")
	if quarters :
		print(f"{quarters} quarter{'s' if quarters > 1 else ' '}")
	if dimes: 
		print(f"{dimes} dimes{'s' if dimes > 1 else ' '}")
	if nickels:
		print(f"{nickels} nickels{'s' if nickels > 1 else ' '}")
	if pennies:
		print(f"{pennies} pennies{'s' if pennies > 1 else ' '}")

