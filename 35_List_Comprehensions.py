#conscice way to create lists in python
#compact & easier to read than normal loops
#format -> expression for value in iterable if condition

doubles = []
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

del doubles
#or
doubles = [x*2 for x in range(1,11)]
print(doubles)

tripples = [y*3 for y in range(1,11)]
print(tripples)

fruits =["apple","orange","bannana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)

numbers = [1,-2,3,-4,5,-6,8,-7]
positive =[num for num in numbers if num >0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num%2 == 0]
odd = [num for num in numbers if num%2 != 0]

print(positive)
print(negative)
print(even)
print(odd)

grades = [85,42,79,90,56,61,30]
passing =[grade for grade in grades if grade >= 60]
print(passing)