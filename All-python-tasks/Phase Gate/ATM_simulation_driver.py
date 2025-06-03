import ATM_simulation_trial

print("WELCOME TO SEMICOLON BANK ATM")
count_try = 0
count_try_amt = 0

while True:
	try:
		bal = int(input("Enter you current balance: "))
		amt = int(input("Enter Withdrawal amount in multiples of 500 and 1000 "))
		print(ATM_simulation_trial.withdrawal(bal, amt))
		print()
		next_round = int(input("Do you wish to do another transaction? 1- Yes 2- no "))
		match next_round:
			case 1:
				amt = int(input("Enter Withdrawal amount in multiples of 500 and 1000 "))
				print(ATM_simulation_trial.more(bal, amt))
			case _:
				break
	except ValueError:
		print("You current balance and withdrawal amount must be a number ")
		count_try += 1
		if count_try == 3:
			print("Try again")
		