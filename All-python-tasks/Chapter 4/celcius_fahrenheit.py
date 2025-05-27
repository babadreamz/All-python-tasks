def temperature():
	result = (f"{'celcius':>15} {'farhenheit':>20}\n")
	result += ( "_" * 40 + "\n")
	for celcius in range (0, 101, 10):
		farhenheit = (9/5) * celcius + 32
		result += f"{celcius:>15.1f} {farhenheit:>20.1f}\n"
			
	return result


'''print(f"{'celcius':>15} {'farhenheit':>20}")
print( "_" * 40)
'''
print(temperature())

