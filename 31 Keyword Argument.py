#keyword arguments -> arument preceeded by identifier
# improves readability
# order of arguments doens't matter

def hello(greeting, title, first, last):
    print(f'{greeting} {title}{first} {last}')

hello(title="Ms.", last= "Runcandel",first="Stella", greeting= "Hello")
#we must make sure positional arguments are before keyword arguments

def get_phone(country,area,first,last):
    return f'{country}-{area}-{first}-{last}'
phone_num = get_phone(country=1,area=234,first=5678,last=9811)
print(phone_num)
