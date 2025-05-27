import random
print("WELCOME TO 'GUESS THE NUMBER' GAME!!")
random_number = random.randrange(1, 1000)
while True:
	user_guess = int(input("Guess my number between 1 to 1000: "))
	if user_guess == random_number:
		print("Congratulations! You guessed the number")	
		break;
	elif user_guess < random_number:
		print("Too low, try again")
	else:
		print("Too high, try again")

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
	