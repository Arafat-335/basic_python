# problam 1 



print("wellcome to my python game !!!") 

quiz = [
	{"question": "your name?","ans": "b"},
	{"question": "where are your city","ans":"c"},
	{"question": "Your favorite color?","ans":"a"},
	{"question":"Your hobby?","ans":"b"},
]
options = [["a) Rafi", "b) Arafat", "c) Hamin", "d) Emon"],
           ["a) Dhaka", "b) Sylhet", "c) Chittagong", "d) Khulna"],
           ["a) Blue", "b) Red", "c) Green", "d) Black"],
           ["a) Reading", "b) Playing games", "c) Traveling", "d) Watching movies"],
]

score = 0

def check_answer(user_guess, correct_ans):
	return user_guess == correct_ans

for question_num in range(len(quiz)):
	print("")
	print(quiz[question_num]["question"])
	for i in options[question_num]:
		print(i)
	guess = input("enter a/b/c/d: ").lower()
	is_correct = check_answer(guess, quiz[question_num]["ans"])
	if is_correct:
		print("correct answer")
		score += 1
	else:
		print("incorrect answer")