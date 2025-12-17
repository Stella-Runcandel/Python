#validate user input
#username can't be over 12 char
#username can't have spaces
#username can't have digits
username = input("Enter a username: ")
username.find(" ") #finds spaces, if no space then gives -1
if len(username) > 12:  #length give slength of string 
    print("Your username cna't be more than 12 characters")
elif not username.find(" ") == 1:
    print("Your ursername can't contain spaces")
elif not username.isalpha(): 
    print("Your usename can't have digits in it")
else:
    print(f'Welcome {username}')