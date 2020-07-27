#An iterator is an object that contains a countable number of values.
# An iterator is an object meaning that you can traverse through all the values.
# an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().

# examples of iterable objects
#tuples, List, dictionaires, you can loop through an iterator
"""mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
