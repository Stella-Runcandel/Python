#property decerator 
#let's us define a method as property (can access it like atribute)
#gives getter,setter and deleter method
#let's us set extra logic

class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f'{self._width:.1f} cm'

    @property
    def height(self):
        return f'{self._height:.1f} cm'
    
    @width.setter
    def width(self,new_width):
        if new_width >0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
    
    @height.setter
    def height(self,new_height):
        if new_height >0:
            self._height = new_height
        else:
            print("Height must be greater than 0")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")
    
rectangle = Rectangle(3,4)
print(rectangle.width,rectangle.height, sep="\n")
rectangle.height =-1
rectangle.height =0
rectangle.width = 4
rectangle.width = 0
rectangle.width = -9
del rectangle.width
del rectangle.height
try:
    rectangle.height
    rectangle.width
except:
    print("Both height and width vars have been deleted")