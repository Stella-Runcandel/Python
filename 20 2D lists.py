fruits = ['apple','orrange','bannana','coconut']
vegetables = ['celery','carrots', 'patatoes']
meats = ['chicken','fish','turkey']
#all are examples of 1D lists

groceries = [fruits, vegetables, meats]
print(groceries)
print(groceries[0])
print(groceries[0][0])

#instead of the list names it could have been the list it self but that's clunky
#to itterate
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()

#we could make list of tupples [ (), (),()]
# or tupple of tupples
# or a tupple made up of sets
