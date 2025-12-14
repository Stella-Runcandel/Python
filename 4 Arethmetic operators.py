#this goes over arthemeetic opertors in python
friends = 0
friends +=1 #this += is an augamentred assignment operator
#could have also been friends = friends + 1
print(f'friend count = {friends}')
friends -= 2 #now we have negative friends ;-;
#could have also been friends = friends - 2
print(f'friend count = {friends}')
friends = 5
friends = friends*3 #coudl have been friends *= 3
print(f'friend count = {friends}')
friends = friends/2 #could have been friends /= 2... welp guess one of them got cut in half
print(f'friend count = {friends}')
#now exponents,
friends = 2
print(f'friend count = {friends}')
friends = friends**2
print(f'friend count = {friends}')
#it could also be
friends **=2
print(f'friend count is now equal to : {friends}')
#modelous? -> remainder after devision mod(10,2) = 0 as 10/2 = 5, no remainder
friends = 10
remainder = friends % 3
print(remainder)
#floor division -> devision rounded down to nearest whole number
friends = 10
friends = friends // 3
print(friends)
#now we have built in functions
x = 3.14159
y = -4 
z = 5
result = round(x) #roudns to ner whole int
print(result)
result= abs(y) #gives absolute value\
print(result)
result= pow(y, z) #base y to the power of z 
print(result)
result= max(x,y,z) #gives max value out of those tested
print(result)
result= min(x,y,z) #gives min value out of those tested
print(result)
#now we import math
import math
print(math.pi)
print(math.sqrt(16))
num = 9.123
num = math.ceil(num) #rounds up
print(num)
num = math.floor(num) #rounds down
print(num)
