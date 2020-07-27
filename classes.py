#Classes
"""class MyClass:
    x = 5
#objects within a class
p1 = MyClass()
print(p1.x)

"""
#Creating a class and calling functions
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40 # changes the age value

p1.myfunc()

print(p1.name)

print(p1.age)

#The self parameter is a reference to the current instance of the class,
#and is used to access variables that belongs to the class.

#It does not have to be named self ,
#you can call it whatever you like,
#but it has to be the first parameter of
#any function in the class:
