number = int(input("Enter a number: "));

old_number = number;
palindrome_number = 0;

while number > 0 :
	unit = number % 10 
	palindrome_number = palindrome_number * 10 + unit
	number = number // 10

if old_number == palindrome_number : 
	print("This number is a palindrome number")
else: 
	print("This is not a palindrome number")