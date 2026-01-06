#Duck Typing -> obj can be treated as a different type if they  have minimum nesseary 
#               atributes and methods to be tread as another type
#               if it looks like a duck , acts like a duck, acts like a duck , it's a duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:
    alive = False
    def speak(self): #chagne horn to speek and all of a sudden it is quacking
        print("Horn")

animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)
