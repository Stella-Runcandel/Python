#super is function, used in child class to call methods form parent class
#allows us to extend functionaly of inherited objects
#let's us use constructor of parent class , and extend functionality
#method overwriting, if child has same method name as parent, childs will be executed..
#use super
class Shapes:
    def __init__(self, color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f'The shape is {self.color}, and {'filled' if self.is_filled else "not filled"}')

class Circle(Shapes):
    def __init__(self,color,is_filled,radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f'It is an area with an area of {3.14*(self.radius**2):.2f} cm')
        super().describe() #tells it to go to parent, and run describ method form it wrt. circ
        #u could also change order put super infornt of print or vise versa


class Square(Shapes):
    def __init__(self,color,is_filled,width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f'It is a square with an area of {(self.width**2):.2f} cm')
        super().describe()

class Triangle(Shapes):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f'It is a triangle with an area of {(self.width*self.height*1/2):.2f} cm')
        super().describe()
        #notice hwo all the clases have something in common ...

circle = Circle('red',True,3.14)
#print(circle.color, circle.is_filled, circle.radius)
#print(f'{circle.radius}cm')
circle.describe()

square = Square("Blue",False, 4)
# print(square.color, square.is_filled, square.width)
# print(f'{square.width}cm')
square.describe()


triangle = Triangle("Yello",True,7,8)
#print(triangle.color)
#print(triangle.is_filled)
#print(triangle.width,"cm")
#print(triangle.height, 'cm')
triangle.describe()
