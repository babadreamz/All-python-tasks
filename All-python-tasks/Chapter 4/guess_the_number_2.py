import random
print("WELCOME TO 'GUESS THE NUMBER' GAME!!")
random_number = random.randrange(1, 1000)
num_of_guesses_lesser = 0
num_of_guesses_higher = 0
while True:
	while True:
		try:
			user_guess = int(input("Guess my number between 1 to 1000 with the fewest guesses: "))
			break
		except ValueError:
			print("enter a number sir, ONLY number(s)")
	if user_guess < random_number:
		if random_number - user_guess <=10:
			print("Too low, but you are close, try again")
		else:
			print("Too low, try again")
		num_of_guesses_lesser = num_of_guesses_lesser + 1
	elif user_guess > random_number:
		if user_guess - random_number <= 10:
			print("Too high, but you are close, try again")
		else:
			print("Too high, try again")
		num_of_guesses_higher = num_of_guesses_higher + 1
	elif user_guess == random_number:
		print("Congratulations, You guessed the number!")
		print()
		total_guesses = num_of_guesses_higher + num_of_guesses_lesser
		if total_guesses <= 10:
			print("Either you know the secret or you got lucky!")
		else:
			print("You should be able to do better!")
		print("""
			Do you want to play again?
			1. No
			2. Yes
			""")
		
		while True:
			try:
				fresh_start = int(input("Select 1 or 2 "))
				break
			except ValueError:
				print("Input must be a number")
		match fresh_start:
			case 1:
				random_number = random.randrange(1, 1000)
				print("Goodbye")
				break
			case 2:
				random_number = random.randrange(1, 1000)
				continue
			case _: 
				random_number = random.randrange(1, 1000)
				while True:
					try:
						second_chance = int(input("Invalid selection, Enter a 1 or 2  "))
						if second_chance == 1:
							print("Goodbye")
							break
						elif second_chance == 2:
							random_number = random.randrange(1, 1000)
							break
						else:
							print("Still invalid, try again")
					except ValueError:
						print("Input must be a number")
				if second_chance == 1:
					break
				else:
					continue
					