#write files in .txt, .json, .csv

txt_data = "I like pizza"
file_path = "output.txt"
#first argument is file=, second is mode=
#with open(file_path, "w") as file: #with is used wrap a block of code open/closes a file ; w is to write a file, r is to read,a is to append, x also wrights, but if file exists then error
    #we gave the file it opens for us (file object) the name file, all cahgnes to file reflect
    #on file obj file = File()
#    file.write(txt_data)
#    print(f"txt file '{file_path}' was created")

employess =["Eugene","Spongebob","Squidward","Patrick"] #tryna paste this in file will give error

#for absolute... we just need location >.< C:\Users\mrram\Desktop
file_path = "C:\\Users\\mrram\\Desktop\\output.txt"
try:
    with open(file_path, "a") as file: 
        file.write('\n'+txt_data) 
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")
#w ovewrites but a appends like file.write ("\n" + text_data)

file_path = "C:\\Users\\mrram\\Desktop\\output.txt"
try:
    with open(file_path, "a") as file: 
        for employee in employess:
            file.write('\n'+ employee) 
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")