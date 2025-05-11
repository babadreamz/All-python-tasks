print()
for side_1 in range(1,21):
	for side_2 in range(side_1,21):
		for hypotenus in range(side_2, 21):
			if side_1**2 + side_2**2 == hypotenus**2: 
				print(f"({side_1}  {side_2}  {hypotenus})")