def integer_sum(number):
	result = 0
	if number < 1 or number > 10000:
		return "Invalid result, enter a number between 1 and 10,000"
	else:	
		for count in range(5):
			digit = number % 10
			number = number // 10
			result += digit
	return result

num = int(input("Enter a number between 1 and 10000: "))
print(integer_sum(num))