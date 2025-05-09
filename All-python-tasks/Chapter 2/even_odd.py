number = int(input("Enter a number"))

if number == 0:
	print('Invalid number')
elif number % 2 == 0:
	print(f"{number} is even")
else:
	print(f"{number} is odd")