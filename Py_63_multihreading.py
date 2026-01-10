#multithreading -> to preform multiple tasks at once
#                   good for io tasks (input/output <reading/writing files, fetching data form api>)
#                   threaing.Thread(target = my_function)

import threading
import time

def walk_dog(name, lname):
    time.sleep(8)
    print(f"You finsihed walking {name} {lname} the dog")

def take_out_trash():
    time.sleep(2)
    print("Please take out the trash")

def get_mail():
    time.sleep(4)
    print("Please get the mail")


#walk_dog()
#take_out_trash()
#get_mail() #all 3 are running on the same thread (main thread)

chose1 = threading.Thread(target=walk_dog, args=("Scooby","Doo"))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)
#now we ahve to start it
chose1.start()
chore2.start()
chore3.start() #tasks finshed absed on time it takes to compelte
print("All chores are complete") #we get this before all threads are finsihed... so
chose1.join()
chore2.join()
chore3.join()
print("All chores are complete/ frfr this time")
#what if funciotns take paramaters? ie dog function now we need to add in args and make it = tupple with arg name
#even it it has more than 1 arg this will work