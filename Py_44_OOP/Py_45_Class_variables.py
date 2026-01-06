#class var -> shared amongs all isntacnes of class (objects)
#   define outside of constructor (i.e __init__)
#   allows us to save data among all objects creted form that class
# each obj has it's own instance variables... i.e self.color = colour
# def__init__(self,colour,...): 
# self.colour = colour <- instance var

class Student:

    class_year_grad = 2029
    num_students = 0


    def __init__(self,name,age): #code in this will always be executed when obj is created
        self.name = name
        self.age = age
        Student.num_students += 1
    

student1 = Student("Stella Runcandel", 21)
student2 = Student("Celestia Valeheart", 9999)
student3 = Student("Jone Doe", 20)
student4 = Student("Jane Doe", 500)
print(student1.name, student1.age)
print(student2.name, student2.age)
print(student1.class_year_grad) #it's better to acess clas var using class rather than obj name
#print(student2.class_year_grad)
print(Student.class_year_grad) #tells us it's class var rather than inst
print(Student.num_students)

print(f'My graduating class of {Student.class_year_grad} has {Student.num_students} students.')
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
