#while loop = executes code while condition is true
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name:")
print(f'Hello {name}')


age = int(input('enter your age: '))

while age < 0:
    print("Age can't be negative")
    age = int(input('enter your age: '))

print(f'You are {age} years old.')

food = input("Enter a food you like (q to quit: )")

while not food == "q":
    print(f'you like {food}')
    food = input("Enter a food you like (q to quit): ")

print('bye')


num = int(input("enter a # between 1 - 10: ")) 

while num < 1 or num > 10:
    print(f'{num} is not valid')
    num = int(input("enter a # between 1 - 10: ")) 

print(f'your number is {num}')
