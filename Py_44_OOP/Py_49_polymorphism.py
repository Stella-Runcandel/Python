#many forms
#2 ways to achieve -> inheratance and Duck typing
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        

    def area(self):
        return 3.14 *(self.radius**2)

class Square(Shape):
    def __init__(self,side):
        self.side = side
        

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,height,base):
        self.height = height
        self.base = base
    
    def area(self):
        return self.base*self.height*1/2
    
class Pizza(Circle):
    def __init__(self,topping,radius):
        self.topping = topping
        super().__init__(radius) #now our pizza is a pizza, a circle and thus a shape

shapes = [Circle(3),Square(4), Triangle(5,6),Pizza("Peporoni",15) ] #each of these is 1 a shape and 2 a circle/triangle/squarie

for shape in shapes:
    print(f'{shape.area()} cm²')

