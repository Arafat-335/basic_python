# problam 1 

questions = ("What is Python language?",) 

options = ( 

    "a. Python is a programming language", 

    "b. This is a human language", 

    "c. This is only one computer language" 

) 

answers = ("a",) 

guesses = [] 

score = 0 

questions_num = 0 

for question in questions: 

    print(question) 

    for option in options: 

        print(option) 

    guess = input("Enter (a/b/c): ") 

    guesses.append(guess) 

    if guess == answers[questions_num]: 

        score += 1 

        print("Correct!") 

    else: 

        print("Incorrect!") 

    questions_num += 1 

print(f"\nYour score is: {score}/{len(questions)}") 

 
 