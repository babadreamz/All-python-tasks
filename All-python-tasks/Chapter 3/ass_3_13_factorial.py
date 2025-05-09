number = int (input("Enter an integer: "))
factorial = 1
if number < 0:
	print("Invalid input")
else:
	for count in range(number):
		factorial = factorial * (number - count)
print(f"{number}! is {factorial}")