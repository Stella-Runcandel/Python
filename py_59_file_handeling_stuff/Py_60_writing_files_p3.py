#csv -> comma seperated files
import csv

employees = [["name","Age","Job"],
             ["Spongebob",30,"Cook"],
             ["Patrik",37,"Unemployed"],
             ["Sandy",27,"Scientist"]]
file_path = "C:\\Users\\mrram\\Desktop\\output.csv"

try:
    with open(file_path, "w",newline="") as file: 
        writer = csv.writer(file) #no output, gota itterate over all rows
        for row in employees:
            writer.writerow(row) #gives new line after each row so we make kwarg newline ="" in the open
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")
except Exception:
    print("Somethign went worng")