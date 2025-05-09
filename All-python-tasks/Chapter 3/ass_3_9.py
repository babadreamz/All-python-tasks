for digits in  range(1):
	
	digit = int(input("Enter numbers: "))

	if digit >= 10_000 and digits <= 99_999: 
	
		first_num = digit // 10000 % 10
		second_num = digit // 1000 % 10
		third_num = digit // 100 % 10
		fourth_num = digit // 10 % 10
		fifth_num = digit % 10

print(f"{first_num} {second_num} {third_num} {fourth_num} {fifth_num}" , end=" ")
