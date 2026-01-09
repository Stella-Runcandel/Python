#decorator -> extends bheaviour of another function
# doens't modifying base funciton
# base function is argument of modifier

#base is get ice cream
#we could use a decorator @get_sprinkes

def add_sprinkels(func):
    def wrapper(*args, **kwargs):
        print("You've added sprinkels 🎊")
        func(*args, **kwargs) #iamgine the func is repalced by the print in get_icecream
    return wrapper #returns function

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You've added fudge 🍫")
        func(*args, **kwargs) #iamgine the func is repalced by the print in get_icecream
    return wrapper #returns function

@add_fudge
@add_sprinkels
def get_icecream(flavour):
    print(f"Here's your {flavour} ice cream🍦")

get_icecream("Chocolate")
