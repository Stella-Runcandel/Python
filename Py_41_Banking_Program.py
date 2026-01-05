#Python Banking Program

def show_balance(balance):
    print("********************")
    print(f"Your ballance is ${balance:.2f}")
    print("********************")


def deposit():
    print("********************")
    depo_amount = float(input("Please enter in amount you'd like to deposite"))
    print("********************")

    if depo_amount<0:
        print("********************")
        print("Invalid Amount")
        print("********************")
        return 0
    else:
        return depo_amount

def withdrawl(balance):
    print("********************")
    withd_amount = float(input("Enter withdrawl ammount"))
    print("********************")
    if withd_amount > balance:
        print("********************")
        print("Insufficent Ballance")
        print("********************")
        return 0
    elif withd_amount <= 0:
        print("********************")
        print("Ammount must be greater than 0")
        print("********************")
        return 0
    else: 
        return withd_amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("********************")
        print("  Banking Program ")
        print("********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")    
        print("********************")
        choise = input("Enter your choice (1-4): ")
        print("********************")

        match choise:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdrawl(balance)
            case '4':
                is_running = False
            case _:
                print("********************")
                print("Invalid input. ")
                print("********************")

    print("********************")
    print("Thank you, have a nice day!")
    print("********************")

if __name__ == "__main__":
    main()