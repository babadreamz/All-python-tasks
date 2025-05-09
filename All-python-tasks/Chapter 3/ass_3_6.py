first_answer = input("What is your problem? ")
second_answer = input("Have you had this problem before(yes or no)? ")

if second_answer.lower() == "yes":
	print('Well, you have it again')
elif second_answer.lower() == 'no':
	print('Well, you have it now')

#formatted_input = second_answer.strip().capitalize()
#if formatted_input == "yes":
#	print('Well, you have it again')
#elif formatted_input == 'no':
#	print('Well, you have it now')