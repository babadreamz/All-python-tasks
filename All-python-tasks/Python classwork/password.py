password = input("Enter your password: ")

if len(password) < 8:
	print("very weak")
elif len(password) == 8:
	print("weak")
elif len(password) > 8 and len(password) <= 16:
	print("strong")
else:
	print("very strong")