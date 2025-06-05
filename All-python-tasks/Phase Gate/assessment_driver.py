import random
from assessment import *

print("Welcome to semicolon Assessment")
playing = True
while playing:
	available_questions = get_available_questions()
	if not available_questions:
		print("No more questions available. Game over.")
		break
	else:
		question = random.choice(available_questions)
		ask_question(question)
		while True:
			print("\nWhat do you want to do next?")
			print("1. Continue")
			print("2. Restart")
			print("3. Exit")
			choice = input("Enter 1, 2, or 3: ").strip()
			if choice == "1":
                		break 
			elif choice == "2":
				reset_game()
				print("\nGame restarted")
				break
			elif choice == "3":
				playing = False
				break
			else:
				print("Invalid input. Please enter 1, 2, or 3.")
	
			score, attempts = get_score()
			print(f"\nYour final score: {score} / {attempts}")
			print("Thanks for playing!")


