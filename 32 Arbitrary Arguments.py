# arbitrary menas idk how many arguemnts user sends at us
# *args -> to accept varying arguments, args means arguments (tupple)
# **kwargs -> kwargs means keyword arguments (dict)
# the * indicates unpacking operator

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
#here *args can be changed to *num... so ig it's more important is the * and the ** 

print(add(2,4,8,9,12,13,4,56,89))

def display_name(*args):
    for arg in args:
        print(arg,end=" ")

display_name("Ms.","Stella","Runcandel")
print()
#kwargs -> 2 unpacking arguments
def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}: {value},', end= " ")
    print()
print_address(nation="Unknown", state="Void", district="Null", city="Darkness", sector="Nihility", zip="000", landmark="Tower of The Void", road="Abyss Street", house_number="42", house_description="Darkness")

#we need args before kwargs or else we get syntax error
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for kwarg in kwargs.values():
        print(kwarg,end=" ")
    print()


#here we must pass all positional then keywords
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake Street",
               apt= "100",
               city = "Detroit",
               state="MI",
               zip="54321")

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if 'apt' in kwargs:
        print(f'{kwargs.get('street')}, {kwargs.get("apt")}')
    else:
        print(f'{kwargs.get("street")}')
    print(f"{kwargs.get("city")} {kwargs.get("state")}, {kwargs.get("zip")}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Fake Street",
               apt= "100",
               city = "Detroit",
               state="MI",
               zip="54321")