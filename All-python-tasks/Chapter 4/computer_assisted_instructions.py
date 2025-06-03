import random
def product(number_1, number_2):
	result = number_1 * number_2
	return result



number_1 = random.randrange(1, 10)
number_2 = random.randrange(1, 10)
while True:
	print(f"How much is {number_1} times {number_2}? ")
	while True:
		try:
			resultant_value = int(input("Answer here: "))
			break
		except ValueError:
			print("Answer must be an integer ")

	if product(number_1, number_2) == resultant_value:
		print("Very Good! ")
		print()
		print("""Do you wish to continue with the multiplication
			1.NO 	or 	2.Yes 	
			""")
		while True:
			try:
				user_choice = int(input("Enter a 1 or a 2: "))
				if user_choice == 1:
					print("Goodbye")
					break
				elif user_choice == 2:
					number_1 = random.randrange(1, 10)
					number_2 = random.randrange(1, 10)
					print(f"How much is {number_1} times {number_2}? ")
					while True:
						try:
							resultant_value = int(input("Answer here: "))
							break
						except ValueError:
							print("Answer must be an number ")

					if product(number_1, number_2) == resultant_value:
						print("Very Good! ")
						print()
						print("""Do you wish to continue with the multiplication
							1.NO 	or 	2.Yes 	
							""")
						continue
					else:
						print("try again")
				else:
					print("invalid selection, must either be 1 or 2 ")
			except ValueError:
				print("Selection must be an integer")			
		break
	else:
		print("please try again")
		
		
