import math
#calc area of circle
radius = float(input("please give me the radius of the circle of interest: "))
area = math.pi * pow(radius,2)
print(f'The area of your circle of radius {radius} is {round(area,4)} units squared. ')
circumfrence  = 2*math.pi*radius
print(f'the circumfrence of your circle is {round(circumfrence,4)} units. ')
#finally find hypotneuse of a triangle
side_1 = float(input('Give me the lenght of side 1 (non hypotenuse): '))
side_2 = float(input('Give me the lenght of side 2 (non hypotenuse, not side 1): '))
hypotenuse = math.sqrt(pow(side_1,2)+pow(side_2,2))
print(f'The hypotenuse of youre triangle is {round(hypotenuse, 2)} units long.')
