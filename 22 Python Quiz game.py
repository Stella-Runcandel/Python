questions = ("How many elements are there in the perodic table of elements?: ",
             "Which animal lays the largest eggs?: " ,
             "What's the most abundant gass in Earth's atmosphere?: ",
             "How many bones are there in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 112 ", "B. 108","C. 118","D.116 "),
           ("A. Whale ", "B.Owl ","C. Crocodile","D. Ostrich"),
           ("Nitrogen","Oxygen","Hydrogen","Helium"),
           ("A. 206", "B. 208 ","C. 203 ","D. 159 "),
           ("A. Earth ", "B. Venus ","C. Moon ","D. Mercury"))

answers = ( "C","D","A","A","B")
gusses = []
score = 0
question_num = 0

for question in questions:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(question)
    for option in options[question_num]:
        print(option, end=" ")
    print()
    guess = input("Enter (A, B, C, D): ").upper()
    gusses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("Your answer is correct!")
    else: 
        print("Sorry that was the wrong answer ;-;")
        print(f"The correct answer to {question} is {answers[question_num]} ")
    question_num += 1
    print()
print('~~~~~~~~~~~~~~~~~~~~~~')
print('     Results     ')
print("Answers: ", end = '')
for answer in answers:
    print(answer, end = " ")
print()
print("Guesses: ", end="")
for guess in gusses:
    print(guess, end=" ") 
print()
score = int(score/len(questions) *100)
print(f"Your final score is {score}% ")