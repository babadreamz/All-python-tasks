total = 0
check = 0
count = 0

gallon = float(input("Enter amount of gallon used or -1 to end: "))

while gallon != -1:
	
	miles = int(input("Enter amount of miles driven: "))
	total = miles / gallon
	print("The miles er gallon for this tank was %.2f" %total)
	

	
	
		