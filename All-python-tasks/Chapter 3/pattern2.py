for row in range (10, 0, -1):
	side_1 = ('*') * row 
	side_2 = (' ') * (row - 1) + ('*') 
	print(f"{side_1:>12}  {side_2:>12}")

