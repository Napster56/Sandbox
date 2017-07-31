"""
Program to create a person class
"""

from datetime import datetime


class Person():
    def __init__(self, first_name="", last_name="", dob="01/01/1900", gender="female"):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.gender = gender

    def calculate_age(self):
        date = datetime.strptime(self.dob, '%d/%m/%Y')
        age = ((datetime.today() - date).days / 365)
        return age

    def __str__(self):
        age = self.calculate_age()
        return "{self.first_name}, who is a {self.gender}, was born on {self.dob} and is {:.0f} old".format(age,
                                                                                                            self=self)


person1 = Person("Dave", "Fields", "10/12/1934", "male")
person2 = Person("Sue", "Jones", "26/01/1966")
person3 = Person("Fred", "Watson", "17/09/1946", "male")
person4 = Person("Leslie", "Farrow", "06/02/1984")
print(person1)


class Lecturer(Person):
    def __init__(self, title="Lecturer", college="Business, Law and Governance", tenure_in_years=1):
        super(). __init__(title, college, str(tenure_in_years))



    def __str__(self):
        return ""


lecturer1 = Lecturer("Senior Lecturer", 12)
