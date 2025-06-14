import cube
from unittest import TestCase
class TestCube(TestCase):
	def test_that_get_cube_function_exists(self):
		cube.get_cube(3)
	def test_that_cube_function_return_correct_answer(self):
		actual = cube.get_cube(5)
		expected = 125
		self.assertEqual(actual, expected)
		actual = cube.get_cube(10)
		expected = 1000
		self.assertEqual(actual, expected)
	def test_that_cube_function_work_between_1_and_10(self):
		self.assertRaises(ValueError, cube.get_cube, 14)
		self.assertRaises(ValueError, cube.get_cube, 13)
	def test_that_cube_function_work_with_negative_numbers(self):
		self.assertRaises(ValueError, cube.get_cube, -8)