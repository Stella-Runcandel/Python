#writing json files
import json
#employess =["Eugene","Spongebob","Squidward","Patrick"] 
employess ={"name":"Spongebob",
            "age":30,
            "job":"cook"
            } 
#json saves as dict
file_path = "C:\\Users\\mrram\\Desktop\\output2.json"
try:
    with open(file_path, "w") as file: 
        json.dump(employess,file,indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("This file already exists!")
except Exception:
    print("Somethign went worng")
#key value pair user is great for .json files
