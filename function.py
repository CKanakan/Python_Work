#Information can be passed into functions as arguments.

#Arguments are specified after the function name, inside the parentheses.
#You can add as many arguments as you want,
#just separate them with a comma.

#The following example has a function with one argument (fname).
#When the function is called, we pass along a first name,
#which is used inside the function to print the full name:

"""
def my_function(fname):
    print(fname + " Refsnes")

my_function("Ronan")
my_function("Emil")
my_function("Lenny")

# Multiple parameters/arguments


def this_function(fname, lname):
    print(fname + " " + lname)

this_function("Brandon", "Vay")


#if he amount of arguments use * to the parameter
def another_function(*kids):
    print("The youngest child is " + kids[2])

another_function("Emil", "Tobias", "Linus")


def country_function(country = "Koen"):
    print("I went to " + country)

country_function("Junen")
country_function("Comso")
country_function()
country_function("Bohivan")

#passing a list into a parameters
def food_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

food_function(fruits)


def return_function(x):
    return 5 * x

print(return_function(3))
print(return_function(5))
print(return_function(17))

"""

# Recursion is a function that calls itself


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example results")
tri_recursion(6)


# Python does not have built in arrays must be imported
# But list can be used as a stand in.
# Must use NumPy
