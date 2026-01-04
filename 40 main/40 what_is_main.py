#if__name__==__"main"__: (this scirpt can be imported or run standalone
                        # Funcations and clases in this module can be reused
                        # withouth the main block of code executing

#e.x libeary -> we want some functions form a libeary , but we don't 
#makes code modular
#leaves no global vars/avoides their execution
#avoides unintended execution


def main():
    #your program goes here
    pass

if __name__=='__main__':
    main()

#explination ->
'''
so every file has a name in python, we can't control it. if the file is run directly it's named main
else it's named the file name (-the py)
if file/script is imported it-> ie. we import script1.py -> __name__ = script1
if checks and makes sure if the file is running directly
aka main means I SAID RUN THIS FILE

import acts as -> searches for file, executs it once, form top to bottom,
if that has if __name__ ... then it won't execute anything  inside the if block as it's nto main file, anything 
outside the if block and if it's solo executable will execute so w eneed to be careful
when making modules and imports
, if not u get ghost execution form libearies and other modules
then it stores it into memory
basically executabels should ahve funcitons, clases and constants

this let's us borrow something form a script withouth runnign the main body of code (main function)
i.e script 2 call script 1's fav food functionw ithotuh running script1.main()

you may notice that if u run a libeary directy i thopens up help , but if u import it it's scielent mabey this is due to if __name...
'''