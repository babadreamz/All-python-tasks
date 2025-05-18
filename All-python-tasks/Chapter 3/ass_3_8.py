sum = 0
product = 1
average = 0
smallest = float("inf")
biggest = float("-inf")

for number in range(4):
	num = int (input("Enter a number "))
	sum += num
	product *= num
	average = sum/4
	if num > biggest:
		biggest = num
	if num < smallest:
		smallest = num
	
print(f"sum is {sum}, product is {product} average is {average}, smallest is {smallest}, biggest is {biggest}")
	