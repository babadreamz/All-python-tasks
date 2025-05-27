 def get_cube(number):
	numbers = range(1, 11)
	if number in numbers:
		return number ** 3
	else:
		raise ValueError
'''def get_cube(number):
	if number in range(1, 11):
		return number**3
	raise ValueError
'''