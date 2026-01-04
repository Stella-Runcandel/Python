#iterable is an object/element which returns it's element one at a time
# thus it can be iterated over in a loop
numbers = [1,2,3,4,5]

for number in numbers:
    print(number, end = " ")
print()

#here we could laso do reversed(numbers)
#and change it to (number, end=" ")
nums = (1,2,3,4,5,6,7)
for num in reversed(nums):
    print(num, end=" ")
print()

fruits ={'bannana', 'straberry','mango','grape'}
for fruit in fruits:
    print(fruit, end=" ")
print()
#as set's are unorded idealy we'd get random output every time; it also cna't be reversed   

name = "Stella Runcandel"
for char in name:
    print(char, end=" ")
print()

name ={"a":1,"b":2,"c":3}
for key in name:
    print(key, end = " ")
print()
for value in name.values():
    print(value, end= " ")
print()
for key,value in name.items():
    print(f'{key} = {value}')
print()
