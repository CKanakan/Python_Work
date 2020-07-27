#Booleans
print(10 < 8)
print(21 > 12)
print(34 == 22)

#If statements with booleans

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))

#List/Arrays
thislist =["apple", "banana", "cherry"]
print(thislist)

# Accessing an item in the Array
thislist =["apple", "banana", "cherry"]
print(thislist[1])


# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
thislist =["apple", "banana", "cherry"]
print(thislist[-1])

# grabbing values within the specify range of the array
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Looping through list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Use this to check if an item is in the array.
thislist = ["apple", "chess", "triangle"]
if "apple" in thislist:
    print("Yes Apple is in this list")

#getting the length of the list
thislist = ["apple", "Brave", "Force"]
print(len(thislist))

#Appending to a list
thislist = ["apple", "Brave", "Force"]
thislist.append("Orange")
print(thislist)

#inserting an item into a specified position
thislist = ["apple", "Brave", "Force"]
thislist.insert(1,"Orange")
print(thislist)

#Remove(), pop() removes items from list

#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#join two list
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Tuples are ordered list and unchangable they use ()
# Synthax for tuples are similar to list
# Cannot add items to it

#Sets are similar but the list can be changed

# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets,
# and they have keys and values.

# example

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)



#Create a dictionary that contain three dictionaries:

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }

}
print(myfamily)

#Create three dictionaries, than create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
