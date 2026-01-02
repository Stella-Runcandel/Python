#collections in python 
# list = [] ordered, unchaning, dupplicates ok
# set = {} unordered, immutable, changable( add /subtract ), duplicates ok
# tuple = () ordered , unchangable, dupplication ok , faster
fruits = ['apple','orrange', 'bannana', 'strawberry']
print(fruits)
print(fruits[2])
print(fruits[::-1])
print(fruits[::2])

for x in fruits: #name it to be singular and the collection to be plural
    print(x)
#print(dir(fruits)) #tells us more about a particular type of "thing"
#print(help(fruits)) #gives description of methods and etc

print(len(fruits))
print('apple' in fruits) #boolean
#fruits[0] = 'pineapple'

#for x in fruits:
#    print(x)

fruits.append('pineapple')
print(fruits)
fruits.remove("pineapple")
print(fruits)
fruits.insert(0, 'pineapple')
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse() #reversed in order of assignment
print(fruits)
pseudofruits = fruits
#alphabetical reverse, sort then reverse
print(fruits.index('apple'))
print(fruits.count("kiwi"))

fruits.clear()

fruitset = {"apple","orrange", " bannana", "coconut"}
print(fruitset)
print(len(fruitset))
print("pineapple" in fruitset)
#trying to acess indexes in set is not allowed 
fruitset.add('pineapple')
print(fruitset)
fruitset.remove(' bannana')
print(fruitset)
fruitset.pop()
print(fruitset)
fruitset.clear()
print(fruitset)

#tupple ordered and unchangable
#der and help
fruits.clear()
fruties = ('taco','tuesday','tornado')
print(len(fruties))
print('pineapple' in fruties)
print(fruties.index('taco'))
print(fruties.count("coconut"))

for frutie in fruties:
    print(frutie)

