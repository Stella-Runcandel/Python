#read files in python (txt,json,csv)
import json
import csv

file_path1 = "C:\\Users\\mrram\\Desktop\\output.txt"
file_path2 = "C:\\Users\\mrram\\Desktop\\output.json"
file_path3 = "C:\\Users\\mrram\\Desktop\\output.csv"
try:
    with open(file_path1, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file wasn't found")
except PermissionError:
    print("You don't ahve permission to read that file")
except Exception:
    print("Something Went Wrong...")

#for json 
try:
    with open(file_path2, "r") as file:
        content = json.load(file)
        print(content["job"])
except FileNotFoundError:
    print("That file wasn't found")
except PermissionError:
    print("You don't ahve permission to read that file")
except Exception:
    print("Something Went Wrong...")

#for csv
try:
    with open(file_path3, "r") as file:
        content = csv.reader(file) #we need to read line by line, iterate over data in file
        print(content) #gives address
        for line in content:
            print(line) #prints line by line but waht if we want a specific column, line[x] x = colum no
            print(line[2])
except FileNotFoundError:
    print("That file wasn't found")
except PermissionError:
    print("You don't ahve permission to read that file")
except Exception:
    print("Something Went Wrong...")