print("Enter two integers: ")
number_1 = int(input("number 1: "))
number_2 = int(input("number 2: "))

if number_1 == number_2:
	print(f"{number_1} is equal to {number_2}")
elif number_1 < number_2:
	print(f"{number_1} is less than {number_2}")
elif number_1 > number_2:
	print(f"{number_1} is greater than {number_2}")
