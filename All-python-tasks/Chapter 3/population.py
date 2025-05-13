population = 8000000
growth_rate = 0.85 /100
print(f"{"Year":<9} {"Population":20} {"Annual growth":<20}")

for years in range (2026, 2126):	
	new_growth = population * growth_rate
	population = population + new_growth
	print(f"{years:<9} {population:<20.2f} {new_growth:<20.2f}")
	print()

	