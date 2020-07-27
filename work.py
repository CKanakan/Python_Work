print("hello world")
if 5 > 2:
    print("five is greater than two.")
x = 5
y = "Hello World"

print(x)
print(y)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Zero"
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)


x = "Python is "
y = "awesome"
z = x + y
print(z)

x = 5
y = 10
print(x*y)

x = "awesome"
#the "x" variable within the function will be a different value of x
#only this function can access this x variable, unless you use global
def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

def thisfunc():
    global x
    x = "fantastic"

thisfunc()

print("Python is " + x)
