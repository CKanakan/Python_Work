#Inheritance

class Person(object):
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
#Use person class to create an object

x = Person("John", "Doe")
x.printname()

#Example of a child class
#adding __init__() mean the child class
#will override the parent's __init__() class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        #you can call the parent by name or using super() and removing self
        self.gradyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of",
        self.gradyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()
