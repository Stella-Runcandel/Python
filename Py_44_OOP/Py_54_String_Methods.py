#class methods -> allow oeprations related to the class
#  take cls as first paramater (refe3rs to class)
#self refers to objects ig u could say

class Student:

    count = 0
    total_gpa = 0


    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += self.gpa

    def get_info(self):
            return f'{ self.name}: {self.gpa}'
    
    @classmethod
    def get_count(cls):
        return f'Total number of students: {cls.count}'
    
    @classmethod
    def get_avg_cgpa(cls):
         if cls.count <= 0:
              return ValueError("No Avg.CGPA Avaliable for 0 or less students")
         else:
              return f"The average cgpa is {cls.total_gpa / cls.count:.3f}"
         
    

student1 = Student("Spongebob",3.2)
student1 = Student("patrick",2.0)
student1 = Student("sandy",4.0)

print(Student.get_count())
print(Student.get_avg_cgpa())
