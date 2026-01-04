# print(dir()) #directory
# __ means/is called dunder
#from script2 import *

#print(__name__)

def fav_food(food):
    print(f"Your fav food is {food}")

def main():
    print("This is script 1")
    fav_food("pizza")
    print("goodbye")

if __name__=="__main__":
    main()
