import random
import string

chars= " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f'Chars: {chars}')
#print (f'Key: {key}')

#encryption
plain_text=input("What is ur message?: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text+= key[index]

print(f'orignal message: {plain_text}')
print(f'Encrypted Message: {cipher_text}')

#Decription
cipher_text=input("What is ur message?: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text+= chars[index]

print(f'orignal message: {plain_text}')
print(f'Encrypted Message: {cipher_text}')
