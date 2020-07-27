#Scope
#local
def myfunc():
    x = 300
    print(x)

myfunc()

#local
def myfunc():
    x = 40
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()


#Global
x = 2000

def myfunc():
    print(x)

myfunc()

print(x)

# Local and Global together
x = 300

def myfunc():
    x = 245
    print(x)

myfunc()

print(x)


# If you use global as a prefix like "global x" the x will
# Belong to the global scope

def myfunc():
    global x
    x = 300

myfunc()
print(x)
# Or to change the global within a function

x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)
