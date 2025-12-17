#methods are like predefiend functions you can run
name = input("Enter your full name: ")
result = len(name) #gives length of string (character count, returns integer)
print(result)
#name. this gives us acess to a ton of other methods
result = name.find(" ") #finds and gives you location/index of first instance of sample character
print(result)
#to find last occurance use .rfind (r -> reverse)
result = name.rfind('l')
print(result)
#if character is not found python gives -1
result = name.find("Z")
print(result)
name = name.capitalize() #returns string , capatilizes first word
print(name)
name = name.upper()#capatilizes all characters of a string
print(name)
name = name.lower() #there is also .lower
print(name)
#.isdigit() returns True or False if a string has only digits result is only boolean
result = name.isdigit()
print(result)
result = name.isalpha() #checks if all of string is alphabets
print(result)
phone_number = input("Gime phone number: ")
result = phone_number.count("-") #counts instances of intrerested characters in string
print(result)
phone_number = phone_number.replace("-" , " ") #replaces specified character with another characer of interest
#print(help(str)) gives u info on how u can manipulate strings
