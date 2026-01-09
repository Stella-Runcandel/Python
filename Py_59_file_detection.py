#file detection
import os #let's python programs interact with os

#there are 2 types of file path 
#relative and absolute
#absolute -> shows directions to file directory/repository form root
#relative to where program execution file is located... inovles use of ./ and ../ , etc...
file_path ="text.sty"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesn't exist")
#what if location changed? thus we need to change file path to... "py_59_file_handeling_stuff/text.sty"
file_path ="py_59_file_handeling_stuff/text.sty"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesn't exist")

#this is all relative...
#absolute time... let's say there is file on my desktop (copy file path, then name it)
file_path="C:/Users/mrram/Desktop/text.txt"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("This is a file")
    else:
        print("This is a directory :c")
else:
    print("That location doesn't exist")