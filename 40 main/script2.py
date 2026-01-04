#from script1 import *
#print(__name__)

from script1 import* 

def fav_drink(drink):
    print(f'Your fav drink is {drink}')

def main():
    print("This is script 2")
    fav_food("sushi")
    fav_drink("coffee")
    print("goodbye")

if __name__=="__main__":
    main()
    