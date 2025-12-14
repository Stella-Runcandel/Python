operator = input("enter in one of the following operators + - / *: ")
num1 = float(input("Enter in a number (float or int) remember this will be num a \n thus a +b or a-b a/b or mod a,b"))
num2 = float(input("enter in a number, remmebr this will be num b , a/b a-b, mod(a,b)"))
if operator == "+" :
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*" :
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
else: 
      print("Operator out of bounds or Num2 can't be 0 for / and %")
      exit()
#Weight converter 
weight = float(input("Enter your weight : "))
unit = input("Is you weight in pounds or kilograms? (K or L): ")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f'you\'re weight is {round(weight,2)} {unit}')
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs"
    print(f'you\'re weight is {round(weight,2)} {unit}')
else:
    print(f'{unit} is an invalid unit')
#temperature converter?
unit = input("Is this temperature in fahrenheit or celsius (F/C)")
temp = float(input("Plz give temperature; it can be an int or float"))
if unit == "C":
    temp = round((temp * 9/5) +32,1)
    unit="Fahrenheit"
    print(f'The temp is {temp}° {unit}')
elif unit == "F":
    temp = round((temp - 32)*5/9,1)
    unit = "Celsius"
    print(f'The temp is {temp}° {unit}')
else: 
    print(f'{unit} is not permited')