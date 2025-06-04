for count in range (1, 10):
	print(f"{count:<3}", end="")
	for n in range (1, 10):
		print(f"{count * n:8}", end="" )
	print()