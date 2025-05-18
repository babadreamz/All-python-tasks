term_count = 0
term = 0
running_total = 0
term_value = 0
total = 0

while True:
	if term % 2 != 0:
		term_value = -(4 / ((2 * term) + 1))
	else:
		term_value = (4 / ((2 * term) + 1))
	term_count += 1
	total = total + term_value
	print(f"{term_count}\t{total:.5f}")
	"""if round(total, 5) == 3.14000:
		print(term_count)
		break
	"""
	
	if round(total, 5) == 3.14159:
		break
	else:
		term += 1
			
