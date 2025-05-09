count = 0
passes = 0
failures = 0
while count <10:
	score = int (input("Enter a 1 or a 2: "))
	while score != 1 and score != 2:
		score = int (input("invalid input, Enter a 1 or a 2: "))
	if score == 1:
		print('Passed')
		passes = passes + 1
	elif score == 2:
		print('Failed')
		failures = failures + 1
	count = count + 1
print(f"Summary\nThe number of students who passed are {passes} \nThe number of students who failed are {failures}")
if passes > 8:
	print("Bonus to instructor")
