largest =  float("-inf")
second_largest =  float("-inf")
for count in range (1,11):
	number = int(input("Enter a number: "))
	if number > largest:
		second_largest = largest
		largest = number
	elif (number > second_largest) and (number != largest):
		second_largest = number

print(largest, "is largest ")
print(second_largest, "is secondlargest ")
	
	