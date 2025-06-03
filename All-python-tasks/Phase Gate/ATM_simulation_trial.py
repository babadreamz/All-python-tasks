TRANS_FEE = 100
def withdrawal (bal, amt):
	def withdrawal_amt(amt):
		count_nonsense = 0
		higher_than_20k = 0	
		while True:	
			if amt >= 500 and amt % 500 == 0:
				if amt <= 20000:
					return amt
					break
				else:
					print(" Try an amount less than 20,000")
					higher_than_20k += 1
					if higher_than_20k == 2:
						break
			else:
				print("Invalid withdrawal amount, enter amount in the multiples of 500 ")
				print("You have 3 more trials")
				count_nonsense += 1
				if count_nonsense == 2:
					break

	def balance (bal):		
		trial_bal_negative = 0
		trial_bal_less = 0
		while True:
			if bal < 0:
				print("Invalid balance, cannot be negative")
				trial_bal_negative += 1
				if trial_bal_negative == 2:
					break
			else:
				return bal





	bal_less_100 = 0
	amt_higher = 0
	while True:
		if bal > amt:
			new_bal = bal - amt - TRANS_FEE
			if new_bal < 100:
				print("Remaining balance must be more than 100 ")
				break
			else:
				print("Transaction Successful!!")
				print(f"Withdrawal amount : {amt}")
				print(f"Withdrawal fee is {TRANS_FEE}")
				print("Remaining balance is: ")
				return new_bal
				break
		else:
			print("Withdrawal amount cannot be more than balance")
			amt_higher += 1
			if amt_higher == 2:
				break
def more(new_bal, amt):
	while True:
		if new_bal != (0.9 * new_bal) or new_bal < 10:
			new_bal = new_bal - amt - TRANS_FEE
			print("Transaction Successful!!")
				print(f"Withdrawal amount : {withdrawal_amt(amt)}")
				print(f"Withdrawal fee is {TRANS_FEE}")
				print("Remaining balance is: ")
				return new_bal
		else:
			break

		
	
