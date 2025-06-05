import random
questions = [
    {
        "No": 1,
        "Question": "what is the capital of Nigeria",
        "Options": {"A": "Lagos", "B": "Calabar", "C": "Abuja", "D": "Makurdi"},
        "Correct_answer": "C"
    },
    {
        "No": 2,
        "Question": "what is the capital of Benue",
        "Options": {"A": "Lagos", "B": "Calabar", "C": "Abuja", "D": "Makurdi"},
        "Correct_answer": "D"
    },
    {
        "No": 3,
        "Question": "what is the capital of Lagos",
        "Options": {"A": "Lagos", "B": "Calabar", "C": "Ikeja", "D": "Makurdi"},
        "Correct_answer": "C"
    },
    {
        "No": 4,
        "Question": "what is the capital of Borno",
        "Options": {"A": "Maiduguri", "B": "Calabar", "C": "Abuja", "D": "Makurdi"},
        "Correct_answer": "A"
    },
    {
        "No": 5,
        "Question": "what is the capital of Kano",
        "Options": {"A": "Lagos", "B": "Calabar", "C": "Abuja", "D": "Kano"},
        "Correct_answer": "D"
    },
    {
        "No": 6,
        "Question": "what is the capital of Kaduna",
        "Options": {"A": "Lagos", "B": "Kaduna", "C": "Port-harcourt", "D": "Lafia"},
        "Correct_answer": "B"
    },
    {
        "No": 7,
        "Question": "what is the capital of Nassarawa",
        "Options": {"A": "Lagos", "B": "Kaduna", "C": "Port-harcourt", "D": "Lafia"},
        "Correct_answer": "D"
    },
    {
        "No": 8,
        "Question": "what is the capital of Rivers",
        "Options": {"A": "Lagos", "B": "Kaduna", "C": "Port-harcourt", "D": "Lafia"},
        "Correct_answer": "C"
    },
    {
        "No": 9,
        "Question": "what is the capital of Anambra",
        "Options": {"A": "Awka", "B": "Kaduna", "C": "Port-harcourt", "D": "Lafia"},
        "Correct_answer": "A"
    },
    {
        "No": 10,
        "Question": "what is the capital of Ogun",
        "Options": {"A": "Lagos", "B": "Abeokuta", "C": "Port-harcourt", "D": "Lafia"},
        "Correct_answer": "B"
    }
]


used_question_no = set()
removed_options = {}
last_question_no = None
question_1_used = False
score = 0
attempted = 0

def get_available_questions():
	available = []
	for question in questions:
		if question["No"] == last_question_no:
			continue
		if question["No"] == 1 and question_1_used:
			continue
		if question["No"] == used_question_no:
			continue
		available.append(question)
def ask_question(question_asked):
	global question_1_used, score, attempted
	question_no = question_asked["Question"]
	removed = removed_option.get(question_no, set())

	attempt_for_this_question = 0
	while attempt_for_this_question < 2:
		print("\nQuestion:", question["Question"])
	for opt1, opt2 in question_asked["Options"].item():
		if opt1 not in removed:
			print(f"{opt1}. {opt2}")
	answer = input("Your answer (A-D): ").strip().upper()
	if answer not in ["A", "B", "C", "D"]:
		print("Please enter only A, B, C and D")
	if answer in removed:
		print("You already tried that option. Pick another")
	attempt_for_this_question += 1
	if answer == question["Correct_answer"]:
		prrint("Correct")
		score += 1
		attempts += 1
		used_question_no.add(question_no)
		question_no == 1
		question_1_used = True
		last_question_no = question_no
		return True
	else:
		print("Wrong Answer")
		removed.add(answer)
		removed_options = [question_no] = removed
		return False
def reset_game():
	global used_question_no, removed_options, last_question_no, question_1_used, score, attempted
	used_question_no = set()
	removed_options = {}
	last_question_no = None
	question_1_used = False
	score = 0
	attempted = 0



def get_score():
	return score, attempts

