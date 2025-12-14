#take user input?, input function; returns string
# input("gime ur name: ")
name = input("Give me your name please: ")
age = input("how old are you?:")
print(f'Hello {name}, how is your day going?')
# print(f"happy {age + 1}th birthday in advance!") why error? age = input, input = str. string + int no go
age = int(age)
age += 1  #type casting str to int
print(f'Happy {age}th birthday in advance')
print(f'so so so... you\'re {age} years old')