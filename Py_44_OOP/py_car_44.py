'''
#object -> a bundle of related attributes ( vars ) and methods( functions )
# you need a class to create many objects
#e.x -> phone, cup , book

#class -> <blueprint> used to design the structure and layout of an object

e.g phone
veriosn number 13
is on -> T or F
price
for cup 
empyt?
temp of liquid
book -> pages
title
methods are a functions whicih belong in an object
obj's represent real wold items
class is blueprint ->designs what obj has, atribtues and what they can do (methods)
#we need to use constructor method (like function) init means initilaize
     #it needs paramaters, self refers to the obj beinc read rn
     # . is atribute access operator
'''
class Car:
    def __init__(self, modle, year, color, for_sale): 
        self.modle = modle
        self.year= year
        self.color = color
        self.for_sale = for_sale

        #methods are actions our objects can preform
    def drive(self):
        print(f"You drive the {self.color} {self.modle}!")
    
    def stop(self):
        print(f"You stopped the {self.color} {self.modle}!")

    def describe(self):
        print(f'{self.year} {self.color} {self.modle}')
