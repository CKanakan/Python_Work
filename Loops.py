"""
#but first if statements
a = 33
b = 200
if b > a:
    print("b is greater than a")

# ELSE if
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")

# ELSE
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")
# And, OR can be used in if statments

# Nested If

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("But not above 20")

# while loops :With the while loop we can execute a
# set of statements as long as a condition is true

"""





"""


i = 1
while i < 6:
    print(i)
    i += 1
#Break statments stop while loops even if the condition is true

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# With the continue statement we can stop the current iteration,
# and continue with the next:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#ELSE
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
"""


"""
#For Loops
#list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#string
for x in "banana":
    print(x)
# break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
#if you put break before print it won't print out banana
# if statments /break/ print is the order in that case
# continue is the same syntax

# range(): To loop through a set of code a specified number of times,
# we can use the range() function,

for x in range(9):
    print(x)

# Specify the range of the value
# Does not print last number "9" in this case
for x in range(3, 9):
    print(x)

# Specify the range of the value
# and increase the increment of the range,
#so in this case it will increase by 3 every time.
for x in range(2, 20, 3):
    print(x)
"""

#Else For
for x in range(6):
    print(x)
else:
    print("it is done")

# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":



#NEsted For Loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
