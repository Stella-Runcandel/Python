#if else statements, do something if conditoin is met, else do something else, 
#can be estended with if elif and else statements, n number of conditons
#we can also nest if and elif and else statements within each other
age = int(input('Enter your age: '))

if age >= 18:
    print("Congralautions, you qualifyi for a credit card!!")
elif age < 0:
    print("The unborn can't be contracted.")
else:
    print(f"Womp Womp, you don't qualify")
#test if user needs food?
response = input("Would you like some food? (Y/N): ")
if response == "Y":
    print("Here you go, your fav food")
else:
    print("I'll prepare food just in case")
#name time
name = input("Please enter your name")
if name == "":
    print("You didn't type anything !!!")
else: 
    print(f'Hello there {name}')
#salfe?
sale = True
if sale:
    print("this item is for sale")
else:
    print("This item isn't for sale")