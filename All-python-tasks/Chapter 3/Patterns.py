for count in range(1,11):
	for stars in range (count):
		print("*", end='')
	print('')

print()

#second triangle
for count in range(10, 0, -1):
	for stars in range(count):
		print('*', end='')
	print('')

print()
	
#third 

for count in range(10, 0, -1):
	print(' ' * (10 - count), end='')
	for stars in range(count):
		print('*',end='')
	print('')

print()
	
print ('fourth')

for count in range(1, 11):
	for space in range (10 - count):
		print('', end='')
	for stars in range(count):
		print('*', end='')
	print('')


