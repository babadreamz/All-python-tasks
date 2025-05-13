dollar_amount = float (input("Enter your dollar amount: "))
if dollar_amount < 0 or dollar_amount > 1:
	print('Invalid amount, must be between $0 and $1')
	dollar_amount = dollar_amount * 100
	change_quarters = dollar_amount / 25
	change_dimes = dollar_amount / 10
	change_pennines = dollar_amount / 100
	print(f"quarters {change_quarters}, dimes {change_dimes}, pennies, {change_pennines}")