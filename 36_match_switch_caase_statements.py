#match-case-statement -> alternative to many if,elif,else statements
# executes some code if value matches a "case"
#cleaner and readable
import random

'''
def day_of_week(day):
    if day ==1:
        return "Sunday"
    elif day ==2:
        return "Monday"
    elif day ==3:
        return "Tuesday"
    elif day ==4:
        return "Wednesday"
    elif day ==5:
        return "Thursday"
    elif day ==6:
        return "Friday"
    elif day ==7:
        return "Saturday"
    else:
        return "Not a valid day"
    
print(day_of_week(random.randint(1,7)))
'''
#what a nightmare :c

def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Not a valid day"
print(day_of_week(random.randint(1,7)))

def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Saturday":
            return True
        case _ :
            return False
        #this coudl also be case "Saturday" | "Sunday" :
        # return True
        #case _: 
        # return False
        #or 
        #or case "Monday" | "Tuesday" | ..."Friday#
        #return False
        #case_:
        #return false


days=["Sunday","Monday","Tuesday", "Wednesday","Thursday", "Friday", "Saturday","Not a day"]
print(is_weekend(random.choice(days)))