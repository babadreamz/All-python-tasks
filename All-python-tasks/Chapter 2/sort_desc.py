num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

numbers = [num1, num2, num3]
numbers_sorted_descend = sorted(numbers, reverse=True)

print("\nNumbers in ascending order:")
for num in numbers_sorted_descend:
    print(num)
