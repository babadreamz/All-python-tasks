num1 = int (input("Enter an integer "))
num2 = int (input("Enter an integer "))
num3 = int (input("Enter an integer "))

total = num1 + num2 + num3
average = total/3
product = num1 * num2 * num3
smallest = min(num1,num2,num3)
largest = max(num1,num2,num3)

print("total is ", total)
print("average is ", average)
print("product is ", product)
print("smallest is", smallest)
print("largest  is ", largest)