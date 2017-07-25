"""
Program to create an employee class
"""


class Employee:
    employee_count = 0  # class variable

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.employee_count += 1

    def display_count(self):
        print("Total Employee %d" % Employee.employee_count)

    def __str__(self):
        return "Name: {}, Age: {}, Salary: {}".format(self.name, self.age, self.salary)

employee1 = Employee("Zara", 25, 25000)
employee2 = Employee("Fred", 37, 35000)
print(employee1)
print(employee2)
print(display_count)