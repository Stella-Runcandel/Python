#A function is a block of reusable code
# place () after a function name to invoke it

#sing happy birthday 3x
'''for x in range(3):
    print("Happy Birthday to You !")
    print( you are old!")
    print("Happy Birthday to you !")
    print()'''

def happy_birthday(name,age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy Birthday to {name}!")
    print()


#we can give function data or var (arguments) through the () 
#but. the function def must have matching set of peramaters or else error
#we need matching no of permaters and arguments, if we miss an argument we get error
#order of peramaters and arguments matter

happy_birthday("Joe",22)
happy_birthday("Jhon",25)
happy_birthday("Doe",27)

def invoice(username, ammount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${ammount:.2f} is due on: {due_date}')

invoice("Stella", 45.67, "12th December 2049")

#return -> ends function and gives data back

def add(x,y):
    z = x+y
    return(z)

def subtract(x,y):
    z = x-y
    return(z)

def multiply(x,y):
    z = x*y
    return(z)

def divide(x,y):
    z = x/y
    return(z)

print(add(1,2), subtract(1,2), multiply(1,2), divide(1,2))

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name

full_name = create_name("Stella", "Runcandel")
print(full_name)
