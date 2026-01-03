#number guessing game
import random as r

lowest_num = 1
highest_num = 100

answer = r.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("Welcome to a number guessing game!!")
print(f'Choose a number, any number between {lowest_num} and {highest_num}')

while is_running:
    guess = input("Enter in your guess: ")
    if not guess.isdigit():
        print(f"Sorry your answer must be a number including or in between {lowest_num} and {highest_num}: ")
    else:
        guess= int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num: 
            print("That number is out or range. ")
            print(f"Sorry your answer must be a number including or in between {lowest_num} and {highest_num}: ")
        else:
            if (guess) == (answer):
                print("Your answer is correct!!")
                print(f'Number of guesses: {guesses}')
                is_running = False
            elif guess<answer:
                print('Too low, try again!')
            elif guess>answer:
                print("Too high, try again!")