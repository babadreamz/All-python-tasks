import employee_payroll
from unittest import TestCase
class TestCube(TestCase):
	def test_employee_payroll_exists(self):
		employee_payroll.employee_details("name", "no_of_hours", "hourly_pay", "fed_tax", "state_tax")

	def test_for_empty_employee_payroll_list(self):
		with self.assertRaises(ValueError):
			employee_payroll.employee_details("", "", "", "", "")

	def test_payroll_statement_is_created(self):
		employee_payroll.employee_details("Hilary Dreamz", 10, 9.7, 0.20, 0.9)	
		self.assertEqual(2, len(employee_payroll.payroll_statement))

	def test_that_number_of_hours_worked_function_worked(self):
		actual = employee_payroll.number_of_hours_worked(0,30.5)
		expected = 30.5
		self.assertEqual(actual, expected)
	
	def test_that_invalid_number_of_hours_worked_are_declined(self):
		with self.assertRaises(ValueError):
			employee_payroll.number_of_hours_worked(0,200)
		with self.assertRaises(ValueError):
			employee_payroll.number_of_hours_worked(0,-20)

	def test_that_current_fed_tax_function_worked(self):
		actual = employee_payroll.current_fed_tax(0,20)
		expected = 0.2
		self.assertEqual(actual, expected)
	
	def test_that_invalid_fed_tax_values_are_declined(self):
		with self.assertRaises(ValueError):
			employee_payroll.current_fed_tax(0,200)
		with self.assertRaises(ValueError):
			employee_payroll.current_fed_tax(0,-20)


	def test_that_current_state_tax_function_worked(self):
		actual = employee_payroll.current_state_tax(0, 20)
		expected = 0.2
		self.assertEqual(actual, expected)
	
	def test_that_invalid_state_tax_values_are_declined(self):
		with self.assertRaises(ValueError):
			employee_payroll.current_state_tax(0,200)
		with self.assertRaises(ValueError):
			employee_payroll.current_state_tax(0,-20)
	
	def test_that_pay_per_hour_function_works(self):
		actual = employee_payroll.pay_per_hour(0, 9.7)
		expected = 9.7
		self.assertEqual(actual, expected)

	def test_that_invalid_pay_per_hour_are_declined(self):
		with self.assertRaises(ValueError):
			employee_payroll.pay_per_hour(0,-5)

	def test_that_set_name_works(self):
		employee_payroll.set_employee_name(0,"Hilary Dreamz")
		expected = "Hilary Dreamz"
		self.assertEqual(employee_payroll.payroll_statement[0] ["name"], expected)
	def test_that_only_strings_are_expected(self):
		self.assertRaises(TypeError, employee_payroll.set_employee_name,1, 56467)
	def test_that_get_payroll_statement_work(self):
		employee_payroll.payroll_statement.clear()
		employee_payroll.employee_details("Hilary", 10, 9.7, 0.2, 0.09 )
		expected = [{"name": "Hilary", "no_of_hours": 10, "hourly_pay": 9.7, "fed_tax": 0.2, "state_tax": 0.09}]
		actual = employee_payroll.get_payroll_statement()
		self.assertEqual(actual, expected)
	def test_that_update_payroll_works(self):
		employee_payroll.payroll_statement.clear()
		employee_payroll.employee_details("Hilary", 10, 9.7, 0.2, 0.09 )
		input_searched = employee_payroll.update_payroll("hilary")
		actual = input_searched["name"]
		expected = "Hilary"
		self.assertEqual(actual,expected )

	def test_that_update_payroll_throws_error_if_not_matched(self):
		employee_payroll.payroll_statement.clear()
		employee_payroll.employee_details("Hilary", 10, 9.7, 0.2, 0.09 )
		self.assertRaises(ValueError, employee_payroll.update_payroll, "Tobi")
