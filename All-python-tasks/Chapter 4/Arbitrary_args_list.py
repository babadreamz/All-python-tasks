def product(*numbers):
	result = 1
	for number in numbers:
		result = result * number
	return result

n1 = 9
n2 = 2
n3 = 10
n4 = 10
print(product(n1,n2,n3,n4))