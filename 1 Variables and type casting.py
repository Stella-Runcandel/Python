#just following along with a tutorial
print("I like sleep")
#there are 4 basic variable types
first_name = "Stella Runcandel"
print(first_name)
food = "ice cream cake"
print(f"Hello world, I am {first_name} and I like {food}")
email = "tacolord@gmail.com"
print(f"You're email is {email}")
age = 21
print(f'you\'re {age} year old')
print(f"What is your phone number?")
price=10.99
print(f'The price is {price}')
quant= 98
print(f"The over all price is {price*quant}")
is_stella = True
is_god = False
print(f"Is stella existancial?\n{is_stella}\nis stella god? \n{is_god}")
if is_stella:
    print(f"welcome to the data base")
else:
    print(f'who the fuck are you?')
del(first_name,food,email,age,price,quant,is_god,is_stella)
#type casting? turn one var type into another
name = "Stella Runcandel"
age = 21
gpa = 9.8965
print(f'your name is {type(name)} your age is {type(age)} your gpa is {type(gpa)}')
print(age,gpa,name)
#what if we trya switch thigns aorund?
gpa = int(gpa)
age = float(age)
print(f'new age type{type(age)} new gpa type {type(gpa)}')
print(age,gpa)
age = str(int(age))
#now if we were to try age +=1 we'd get error, we can only concatonate strings, not strigns and other data type
print(type(age),age)
#bool are either true of false; 0,"" = false, everythign else is true
name = bool(name)
print(type(name),name)
#normaly/most of item input = str
#we may want to convert it into other types
del(name, age, gpa)