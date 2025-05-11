decimal = 0
power = 0 

string_binary = input("Enter binary digits: ")
if not all(d in '01' for d in string_binary):
	print('invalid, only 0s and 1s are allowed')
else:
	index = len(string_binary) - 1
	
	while index >= 0 :
		digit = string_binary[index]
		decimal = decimal + int(digit)*(2 ** power)
		power = power + 1
		index -= 1

	print(f"{decimal}")
