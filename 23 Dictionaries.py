#dictionary - has {key:value} pairs
# no duplication allowed

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Bejing",
            "Russia":"Moscow"}

#cheeck if key is in dictionary
print(capitals.get('India'))
print(capitals.get('Japan'))
if capitals.get('Japan'):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
print(capitals)
capitals.update({"USA":"Detroit"})
print(capitals)
capitals.pop("China")
print(capitals)
capitals.popitem()
print(capitals)
capitals.clear()

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Bejing",
            "Russia":"Moscow"}
#to get all keys?
keys = capitals.keys()
print(keys)

for key in keys:
    print(key)

values = capitals.values()
print(values)
for value in values: #or we could have just used capita.values() instead of values
    print(value)

items = capitals.items() #returns list of tupples... 2D list
print(items)
for key,value in capitals.items():
    print(f'{key} : {value}')