number = 4
new_pie = 0
total_div = 0
for counter in range(1):
	for count in range (3, 10, 2):
		div = (number/count)
		total_div = total_div + div
	pie = number - total_div
	print(pie)

	