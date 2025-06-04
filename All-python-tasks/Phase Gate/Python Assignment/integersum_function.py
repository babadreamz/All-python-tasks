def integer_sum(number):
	if number < 1 or number > 10000:
		print("Invalid result, enter a number between 1 and 10,000")
	else:
		digit_1 = number % 10
		number = number // 10
		digit_2 = number % 10
		number = number // 10
		digit_3 = number % 10
		number = number // 10
		digit_4 = number % 10
		number = number // 10
		digit_5 = number % 10

		result = digit_1 + digit_2 + digit_3 + digit_4 + digit_5
		return result

number = int(input("Enter a number between 1 and 10,000: "))

print(integer_sum(number))