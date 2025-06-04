accounts = []
#accounts = [{"name": name, "account_number": account_number, "balance": balance}]
def create_accounts(name, account_number, balance=0):
	if not name or not account_number:
		raise ValueError("name and number cannot be empty") 
	account = {"name": name, "account_number": account_number, "balance": balance}
	accounts.append(account)
	
def deposit(index, amount):
	if amount <= 0:
		raise ValueError("Deposit amount must be more than 0 ")
	accounts [index]["balance"] += amount
	return accounts[index]["balance"] 
def withdrawal(index, amount):
	if amount <= 0:
		raise ValueError("Withdrawal amount must be more than 0 ")
	elif amount > accounts[index]["balance"]:
		raise ValueError("Withdrawal amount cannot be more than the balance ")
	accounts [index]["balance"] -= amount
	return accounts [index]["balance"] 
def getBalance(index):
	if index < 0 or index >= len(accounts):
		raise ValueError
	balance = accounts [index]["balance"]
	return balance
	
def setName(index, name):
	if not isinstance(name, str):
		raise TypeError("Name must be a string ")
	accounts[index]["name"] = name
def setAccountNumber(index, account_number):
	if not isinstance(account_number, str):
		raise TypeError("account number must be a string ")
	accounts[index]["account_number"] = account_number
def get_all_accounts():
	if not accounts:
		raise ValueError
	return accounts	
def search_by_name_or_account_number(search_input):
	for account in accounts:
		if search_input.lower() == account["name"].lower() or search_input == account["account_number"]:
			return account
		raise ValueError ("Search does not match either an account")