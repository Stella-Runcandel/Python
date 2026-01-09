#import py_car as p
from py_car_44 import Car
#from py_car import *

car1 = Car("mustang", 2026, "Purple", False)
car2 = Car("Corvet",2025,"Blue",True)
car3 = Car("Charger", 2026,"Yellow", True)

print(car1.color)
print(car2.color, car2.for_sale)
print(car3.modle)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car2.drive()
car3.drive()
car1.stop()
car2.stop()
car3.stop()
car1.describe()
car2.describe()
car3.describe()