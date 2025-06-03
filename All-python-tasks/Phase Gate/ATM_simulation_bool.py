TRANS_FEE = 100

def withdrawal_amt(amt):
	count_nonsense = 0
	higher_than_20k = 0	
	while True:	
		if amt >= 500 and amt % 500 == 0:
			if amt <= 20000:
				True
				break
			else:
				False
				higher_than_20k += 1
				if higher_than_20k == 2:
					break
		else:
			False
			count_nonsense += 1
			if count_nonsense == 2:
				break

def balance (bal):
	trial_bal_negative = 0
	trial_bal_less = 0
	while True:
		if bal < 0:
			False
			trial_bal_negative += 1
			if trial_bal_negative == 2:
				break
		elif bal >= 0 and bal < 500:
			False
			trial_bal_less += 1
			if trial_bal_less == 2:
				break
		else:
			True

def withdrawal (bal, amt):
	bal_less_100 = 0
	amt_higher = 0
	while True:
		if balance (bal) > withdrawal_amt(amt):
			new_bal = balance (bal) - withdrawal_amt(amt) - TRANS_FEE
			if new_bal < 100:
				False
			else:
				print("Transaction Successful!!")
				print(f"Withdrawal amount : {withdrawal_amt(amt)}")
				print(f"Withdrawal fee is {TRANS_FEE}")
				print("Remaining balance is: ")
				return new_bal
				break
		else:
			print("Withdrawal amount cannot be more than balance")
			amt_higher += 1
			if amt_higher == 2:
				break