age = int(input("Enter your age in years: "))

max_heart_rate = 220 - age

lower = max_heart_rate * 0.50
upper = max_heart_rate * 0.85

print(f"\nMaximum Heart Rate: {max_heart_rate} beats per minute")
print(f"\nTarget Heart Rate Range: {lower:.0f} - {upper:.0f} beats per minute")
