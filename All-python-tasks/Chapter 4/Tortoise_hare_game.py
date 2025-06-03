import random
def tortoise_move():
	movement_tortoise = random.randrange(1, 11)
	return movement_tortoise

def hare_move():
	movement_hare = random.randrange(1,10)
	return movement_hare

print('''
	BANG !!!!
	AND THEY'RE OFF !!!!	
	''')
tortoise_position = 1
hare_position = 1
while True:
	move_t = tortoise_move()
	move_h = hare_move()

	tortoise_position += move_t
	hare_position += move_h

	tortoise_position = max(1, min(tortoise_position, 70))
	hare_position = max(1, min(hare_position, 70))

	track = [" "] * 70
	if tortoise_position == hare_position:
		track[tortoise_position - 1] = "OUCH!!"
	else:
		track[tortoise_position - 1] = "T"
		track[hare_position - 1] = "H"
	print(" ".join(track))
	if tortoise_position >= 70 and hare_position >= 70:
		print("Its a tie, but tortoise gets the win")
		break
	elif tortoise_position >= 70:
		print("TORTOISE WINS! YAY!!")
		break
	elif hare_position >= 70:
		print("Hare wins. Yuch")
		break