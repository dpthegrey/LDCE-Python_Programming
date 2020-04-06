# create a class named Employee
class Employee:

    # initialize the attributes
    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    # set the attributes
    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def set_department(self, department):
        self.__department = department

    # return the attributes
    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    # return the object's state as string
    def __str__(self):
        return 'Name: ' + self.__name + \
            '\nsalary: ' + self.__salary + \
            '\nDepartment: ' + self.__department


# Create three employee objects
emp1 = Employee('name', 'salary', 'department')

# Createthree Employee objects for each attributes
emp1.set_name('Jon')
emp1.set_salary('1696969')
emp1.set_department('Computer Department')


print()
print(emp1)
