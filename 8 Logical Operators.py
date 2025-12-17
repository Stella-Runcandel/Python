#3 logical operators -> or , and & not (inverts condition)
#use of or operator 
temp = 26
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancled")
else:
    print("The outdoor event is still scheduled")
#use of and operator (all conditons related must be true)
temp = 20
is_sunny = True
if temp >= 28 and is_sunny:
    print("It's Hot outside >.<")
    print("It's SUNNY")
elif temp <= 0 and is_sunny:
    print("It's Cold outside >.<")
    print("It's SUNNY")
elif 28 > temp > 0 and is_sunny: #here something interesitn ghappend we coudl have typed temp < 28 and temp > 0 and is_suny but it can be simplified
    print("It's Warm outside >.<")
    print("It's SUNNY")
#now it's time for implimentation of not operators
if temp >= 28 and not is_sunny:
    print("It's Hot outside >.<")
    print("It's Cloudy")
elif temp <= 0 and not is_sunny:
    print("It's Cold outside >.<")
    print("It's Cloudy")
elif 28 > temp > 0 and not is_sunny: 
    print("It's Warm outside >.<")
    print("It's Cloudy")
#conditional EXPRESSIONS 
#one line short cut for if else statements (Ternary Operator)
# return x if condition (is true) else return y 
#< x if condition else y>
num = -5
a = 6
b = 9
print("positive" if num > 0 else "negative")
result = "even" if num % 2 == 0 else "odd"
print (result)
max_num = a if a > b else b
min_num = a if a < b else b
print(min_num)
print(max_num)
age = 25
status = "Adult" if age > 18 else "Child"
print(status)
temperature = 30
weather = "Hot" if temperature > 20 else "Cold"
print(weather)
user_roll = "Admin"
access_level = "Full Access" if user_roll == "Admin" else "Limited Access"
print(access_level)
