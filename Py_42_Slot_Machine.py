#Python Slot Machine
import random

def spin_row():
    symbols =['🍋', '⭐', '🔔', '🍒', '🍉']
    return [random.choice(symbols) for symbol in range(3)]
    

def print_row(row):
    print("****************")
    print(" | ".join(row))        
    print("****************")


def get_payout(row, bet): #result analysis of print_row
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet*3
        elif row[0] =="🍉":
            return bet*4
        elif row[0] =="🍋":
            return bet*5
        elif row[0] =="🔔":
            return bet*10
        elif row[0] =="⭐":
            return bet*20
        else:
            return 0
    else: return 0

def main():
    ballance = 100
    print("***************************")
    print("Welcome to Python Slots   ")
    print("Symbols: 🍋 ⭐ 🔔 🍒 🍉 ")
    print("***************************")

    while ballance >0:
        print(f'Current balance: ${ballance}')

        bet = input("Place your bet ammount: ")
        if not bet.isdigit():
            print("Invalid bet ammount. +ve Integeers only")
            continue
        bet = int(bet)

        if bet > ballance:
            print("Insufficent Funds")
            continue
        if bet <= 0:
            print("Bet must be > 0")
            continue

        ballance-=bet
        row = spin_row()
        print("Soinning... \n")
        print_row(row)

        payout = get_payout(row,bet)
        if payout >0:
            print(f'You won ${payout}')
        else:
            print("Sorry you lost this round")
        ballance+= payout

        play_again = input(("Do you want to play again (y/n):  "))
        if play_again.lower() != "y":
            break
    print("********************************************")
    print(f'Game over, your final ballance is ${ballance}')
    print("*********************************************")


if __name__=="__main__":
    main()