#membership opertoars -> in, not in 
# check if value or var is found in a sequence or not
#we can check lists, tuples, sets and dicts
#return boolean


word = "apple"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f'The letter: {letter} is in the secrete word!!')
else:
    print(f'There is no {letter} in the secrete word!!')

students = {"spongebob","Patric","Sandy"}

student = input("Enter in the name of a student")

if student in students:
    print(f'{student} is in students')
else:
    print(f'{student} is not in students.')

grades = {"Sandy":"A", "Squidwrd":"B","Spongebob":"C","Patrik":"D"}

if student in grades.keys():
    print(f'{student}\'s grade is {grades.get(student)}')
else:
    print(f'{student} was not found.')

email = "name@email.com"
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
