import random
import time
count = 0
count_correct = 0
count_wrong = 0
start_time = time.time()
while True:
	number_1 = random.randint(1, 10)
	number_2 = random.randint(1, 10)
	if number_1 > number_2:
		quotient = number_1 - number_2
		counter = 0
		while True:
			print(f"what is {number_1} - {number_2} ?")
			while True:
				try:
					user_answer = int(input("Enter your answer here:  "))
					break
				except ValueError:
					print("Answer must be an integer ")
					print(f"what is {number_1} - {number_2} ?")
			if user_answer == quotient:
				count_correct += 1
				break
			else:
				counter = counter + 1	
				if counter > 1:
					break
				
	else:
		continue
	count += 1
	if count == 10:
		break;
	
print(f"The score is {count_correct}/{count}" )

end_time = time.time()
total_time = end_time - start_time
print(f"The total time is {total_time:.2f} seconds")