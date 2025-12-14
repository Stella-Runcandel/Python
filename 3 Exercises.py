#calculate area of a rectangel
length = float(input("please enter length of rectangle: "))
width = float(input("please enter width of rectangel: "))
area = length * width
print(f'The area of you rectangle of width {width} and length {length} is {area} units²')
#we type cast as float as otherwise, they'd be strings and we can't multiply those
#shopping cart
item = input("enter item of interest: ")
price = float(input(f'give price of {item}: '))
quantity= int(input(f'give me quantitiy of {item}: '))
total = price * quantity
print(f"the total price of your cart for {quantity} {item}'s is $ {total} ")
#madlibs time
adjective = input("put in a descreptive word")
adjective2 = input("put in a descreptive word")
adjective3 = input("put in a descreptive word")
noun1 = input("person, place or thing")
verb = input("actionnnn")
print(f'Today I went to a {adjective} zoo.')
print(f'In an exebhite i saw a {noun1}')
print(f'{noun1} was {adjective2} and {verb}.')
print(f'I was {adjective3}.')
