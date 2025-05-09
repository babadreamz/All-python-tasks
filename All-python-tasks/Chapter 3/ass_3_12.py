number = int(input("Enter a number: "));

original = number;
reversed = 0;

while number > 0 :
	digits = number % 10 
	reversed = reversed * 10 + digits
	number = number // 10

if original == reversed : 
	print("This number is a palindrome number")
else: 
	print("This is not a palindrome number")