class Student:
    """Create a simple Student class"""
    def __init__(self, first='', last='', id=0):     # constructor method
        self.first_name = first
        self.last_name = last
        self.id = id

    def update(self, first='', last='', id=0):
        if first:
            self.first_name = first
        if last:
            self.last_name = last
        if id:
            self.id = id

    def __str__(self):          # string method for printing
        return "{} {}, ID:{}".format(self.first_name, self.last_name, self.id)

student1 = Student("Patrick", "Stewart", 3001)
student2 = Student("Lucy", "Diamond", 3002)

print(student1)
print(student2)