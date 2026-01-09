#exception -> interupts flow of program
# zero division, type error, value error, ...
# 1. try , 2. except, 3. finally
try:
    number = int(input("Enter in a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Please enter in only numbers")
except Exception: #badd practice, gives vague answer we odn't know what went worng
    print("Somethign went worng")
finally: #always executes
    print("Do some cleanup here")