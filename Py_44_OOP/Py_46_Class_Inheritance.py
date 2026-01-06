#inheritance -> allows class to inherit atributes and methods form other clases
#               helps with code reusability and extensibility
#               class child(Partent) aka sub(Super) clases 

class Animal: #let's us easiably write , read and change code and effect multiple clases
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating!') 

    def sleep(self):
        print(f'{self.name} is asleep!') 

class Dog(Animal): #can have their own differnt atri and method
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Mouse(Animal):
    def speak(self):
        print("Squeek")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("mickey")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak() 