import random
print("WELCOME TO 'GUESS THE NUMBER' GAME!!")
random_number = random.randrange(1, 1000)
counter_low = 0
counter_high = 0
while True:
	user_guess = int(input("Guess my number between 1 to 1000: "))
	if user_guess == random_number:
		print("Congratulations! You guessed the number")
		print(""" 
			Do you want to play again?
			1 - Yes
			2 - No
			""")
		fresh_start = input()
		while True:
			match fresh_start:
				case '1': 
					random_number = random.randrange(1, 1000)
					continue
				case '2': 
					print("Goodbye")
					break
				case _: 
					print("Invalid selection")
					break				
		break;
	elif user_guess < random_number:
		print("Too low, try again")
	counter_low = counter_low + 1
	else:
		print("Too high, try again")
	counter_high = counter_high + 1
		count_total = counter_high + counter_low
	
if count_total <= 10:
	print("Either you know the secret or you got lucky!") 
else:
	print("You should be able to do better!" Why should it take no more than 10 guesses? ") 


'''
print(""" 
	Do you want to play again?
	1 - Yes
	2 - No
	""")
	fresh_start = int (input())
	match fresh_start:
		case 1: 
'''
	