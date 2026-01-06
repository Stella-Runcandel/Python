#static methods -> methods wich belong to a class, rather than objects (instances) from that class
# used for utility

#instance methods -> best for operatons on instances of a class (def askadf(self):)
#static methods -> for utility functions which don't need to access class data

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f'{self.name} = {self.position}'
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cook","Cashier","Janitor"]
        return position in valid_position
    
employee1 = Employee('Eugune','Manager')
employee2 = Employee('Sponge Bob','Cook')
employee3 = Employee('Squidward','Cashier')
employee4 = Employee('Patrick','Janitor')


print(Employee.is_valid_position("cheese"))
print(
employee1.get_info(),
employee2.get_info(),
employee3.get_info(),
employee4.get_info(),sep="\n") #notice how we need to call/make an object to use get_info method
#but with static we cand irectly check

print(Employee.is_valid_position("position"))
