import random

options = ('rock', 'paper', 'scissors')
game_not_won = True
Playing = True
while Playing:

    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a choice ( rock, paper or scissors): ")

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    if player == computer:
        print("It's a tie")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
        print("You win")
    else:
        print('You loose!')
    
    play_again = input("Would you like to play agian (y/n): ")
    pa_options = ("y","n")
    while play_again.lower() not in pa_options:
        play_again=input("Type in only y or n") 
    if play_again.lower() == 'n':
        Playing = False
    #or we could have done if not input("Would you like to play again (y/n)").lower() == 'n': 
        #playing = false

print("Thanks for playing!!!")
