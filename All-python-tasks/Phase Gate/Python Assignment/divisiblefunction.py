
def categorize_number(*args, divisible_by=5):
	multiples =[]
	count = 0
	for num in args:
		if num % divisible_by == 0:
			multiples.append(num)
			count +=1 
			
		
	if count > 0 :
		return tuple(multiples)
	else: 
		return 'No divisible number found'















'''print(categorize_number(15, 10, 25, 20))'''
