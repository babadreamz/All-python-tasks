import bank_app
import unittest
class TestBank(unittest.TestCase):
	def test_for_empty_list_values(self):
		with self.assertRaises(ValueError):
			bank_app.create_accounts("", "",)

	def test_that_account_is_created(self):
		bank_app.create_accounts("Hilary", "0817823")	
		self.assertEqual(1, len(bank_app.accounts))

	def test_that_deposit_function_works(self):
		actual = bank_app.deposit(0,100)
		expected = 100
		self.assertEqual(actual, expected)
		actual = bank_app.deposit(0,50000)
		expected = 50100
		self.assertEqual(actual, expected)

	def test_that_checks_if_invalid_deposits_are_declined(self):
		self.assertRaises(ValueError, bank_app.deposit, 0,-100)
#	Another way to do it
		with self.assertRaises(ValueError):
			bank_app.deposit(0,0)

	def test_that_withdrawalfunction_works(self):
		bank_app.accounts.clear()
		bank_app.create_accounts("Hilary", "0817823", 1000)
		actual = bank_app.withdrawal(0,500)
		expected = 500
		self.assertEqual(actual, expected)

	def test_to_see_if_can_withdraw_more_than_available_balance(self):
		with self.assertRaises(ValueError):
			bank_app.withdrawal(0,1200)

	def test_that_get_balance_work(self):
		bank_app.accounts.clear()
		bank_app.create_accounts("Hilary", "0817823", 1000)
		actual = bank_app.getBalance(0)
		expected = 1000
		self.assertEqual(actual, expected)
	
	def test_that_you_cant_getBalance_outside_index_length_gives_an_error(self):
		self.assertRaises(ValueError, bank_app.getBalance,9)
	
	def test_that_setName_function_work(self):
		bank_app.setName(0,"Hilary")
		expected = "Hilary"
		self.assertEqual(bank_app.accounts[0]["name"], expected)

	def test_that_only_strings_are_accepted_to_setName(self):
		self.assertRaises(TypeError, bank_app.setName, 0, 3456)
	
	def test_that_set_account_number_function_work(self):
		bank_app.setAccountNumber(0,"081783624")
		expected = "081783624"
		self.assertEqual(bank_app.accounts[0]["account_number"], expected)
	def test_that_only_strings_are_accepted_to_setAccountNumber(self):
		self.assertRaises(TypeError, bank_app.setAccountNumber, 0, 3456)
	def test_that_getAllAccount_works(self):
		bank_app.accounts.clear()
		bank_app.create_accounts("Hills","phone No", 1000)
		expected = [{"name": "Hills", "account_number": "phone No", "balance": 1000}]
		actual = bank_app.get_all_accounts()
		self.assertEqual(actual, expected)
	def test_that_get_all_accounts_doesnt_return_empty_list(self):
		bank_app.accounts.clear()
		self.assertRaises(ValueError, bank_app.get_all_accounts)
	
	def test_that_search_by_name_or_acctNumber_works(self):
		bank_app.accounts.clear()
		bank_app.create_accounts("Hills","308090", 1000)
		input_searched = bank_app.search_by_name_or_account_number("hills")
		actual = input_searched["account_number"]
		expected = "308090"
		self.assertEqual(actual,expected )
		
		input_searched = bank_app.search_by_name_or_account_number("308090")
		actual = input_searched["name"]
		expected = "Hills"
		self.assertEqual(actual,expected )

	def test_to_check_if_search_by_name_or_number_throws_error_when_not_matched(self):
		bank_app.accounts.clear()
		bank_app.create_accounts("Hills","308090", 1000)
		self.assertRaises(ValueError, bank_app.search_by_name_or_account_number, "Hilary")