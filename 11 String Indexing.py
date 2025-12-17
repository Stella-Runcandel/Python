#string indexing -> accessing elements of a sequence using [] (indexing operator)
# [star : end : step]
credit_card_no = "1234-5678-9012-3456"
print(credit_card_no[0]) #print's the element at the 0th index of credit card no
#if there is only one value in [] withouth any collones (:) it's asumed u gave start position
#thus u only get element at tart position
print(credit_card_no[0:4]) #prints digits form index 0 to n-1 , n refers to the end field value in []
#you can ommit the 0, python will asume starting position is begining of string
print(credit_card_no[:4])
print(credit_card_no[5:9]) #gives us elements form index 5 to but excluding 9
print(credit_card_no[5:]) #gives elemtns form index 5 to and including end of string
#no need to list ending index, jsut add colon, python assumes until end of string
#indexing can also be negative
print(credit_card_no[-4]) #will give element of n form end of string , ie -1 is 6, -2 is 5...
print(credit_card_no[::2])#python assumes start to end of sequence, also assumes step 2
#starts form element at index of 0, the goes to start + 2, basicly ap with a = start, d = 2
#n = until string ends or b is not out of bounds of index length; b = a(n-1)d
#make program to get last 4 digits of credit card no
last_digits = credit_card_no[-4:]
print(f"xxxx-xxxx-{last_digits}")
#let's reverse characters in string
credit_card_no = credit_card_no[::-1] #reverses string
print(credit_card_no)