import ATM_simulation
import unittest
class TestATM_simulation(unittest.TestCase):

	def test_for_balance(self):
		actual = ATM_simulation.withdrawal_amt(50000)
		expected = 50000
		self.assertEqual(actual, expected)