import random # must import random to use the random module

x = int(5)
y = float(23.7)
z = str("Hello World")
print(x , y, z)

#these are number types
x = 1 # int
y = 2.8 # float
z = 1j # complex

#Assign string to variable
a = "Hello"
print(a)

#finding the character in a position within a string
a = "Hello, World!"
print(a[1])

#Slicing an string
a = "Hello, World!"
print(a[3:9])

#negative indexing - starts at character[5] and goes backwards
a = "Hello, World!"
print(a[-5:-2])

# Len() returns the length of a string
a = "Hello, World!"
print(len(a))

# removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip())

# Splits the string into substring
a = " Hello, World! "
print(a.split(","))


#checks if a phrase in the string, uses in not in

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# lower() changes the string to lower case
# upper() changes the string to upper case

#replace characters
a = "Hello, World!"
print(a.replace("H", "J"))

#random
print(random.randrange(1,10))

#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#This is data casting, data-type (value) and it will convert it
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
