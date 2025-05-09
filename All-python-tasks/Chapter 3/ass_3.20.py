decimal = 0
power = 0 

binary_str = input("Enter binary digits: ")
index = len(binary_str) - 1

while index >= 0 :
	digit = binary_str[index]
	decimal += int(digit)*(2 ** power)
	power += 1
	index -= 1

print(f"{decimal}")
