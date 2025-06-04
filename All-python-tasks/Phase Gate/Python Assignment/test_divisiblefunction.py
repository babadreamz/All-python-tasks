import divisiblefunction
from unittest import TestCase
class TestDivisibleFunction(TestCase):
	def test_that_categorize_number_funtion_exists(self):
		divisiblefunction.categorize_number(14, 17, 12, divisible_by=5)
	def test_that_that_categorize_number_funtion_return_correct_answer(self):
		actual = divisiblefunction.categorize_number(10, 15, 23,25,37)
		expected = (10,15,25)
		self.assertEqual(actual, expected)