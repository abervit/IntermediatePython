# Tuples (collection data type) - ordered, immutable, allows duplicate elements
# Tuple can't be changed after its creation. Also is used for objects that belong together

"""Creating a tuple"""
mytuple = ("Max", 28, "Boston")
print(mytuple)  # --> ('Max', 28, 'Boston')

"""Parenthesis are optional, so we can leave them away"""
mytuple = "Max", 28, "Boston"
print(mytuple)  # --> ('Max', 28, 'Boston')

"""If we have 1 element even in parenthesis, it`s not recognised as tuple, but string. We have to add comma in the end"""
mytuple = "Max"
mytuple1 = "Max",
mytuple2 = ("Max")
mytuple3 = ("Max",)
print(type(mytuple))  # --> Max <class 'str'>
print(type(mytuple1))  # --> ('Max',) <class 'tuple'>
print(type(mytuple2))  # --> Max <class 'str'>
print(type(mytuple3))  # --> ('Max',) <class 'tuple'>

"""We can create a tuple with tuple() function from iterable for example - list"""
mytuple = tuple([1, 2, 3, 4, 5, 6])
print(mytuple)  # --> (1, 2, 3, 4, 5, 6)
mytuple = tuple("one, two")
print(mytuple)  # --> ('o', 'n', 'e', ',', ' ', 't', 'w', 'o')
mytuple = tuple({1, 2, 3, 2, 1})
print(mytuple)  # --> (1, 2, 3)

"""Accessing elements by referring index"""
mytuple = tuple(["Max", 28, "Boston"])
item = mytuple[1]
print(item)  # --> 28

"""We can't change elements of our tuple. It's immutable"""
mytuple = tuple(["Max", 28, "Boston"])
# mytuple[1] = "NR"
print(mytuple)  # --> TypeError: 'tuple' object does not support item assignment

"""Iteration"""
mytuple = tuple(["Max", 28, "Boston"])
for i in mytuple:
    print(i)  # --> prints out all elements one by one of the tuple

"""Checking if element is inside our tuple"""
if "Max" in mytuple:
    print("yes")  # --> yes
else:
    print("no")

"""Other method of tuple"""
mytuple = ("a", "p", "p", "l", "e")
print(len(mytuple))  # --> 5  == length

print(mytuple.count("p"))  # --> 2 == count

print(mytuple.index("p"))  # --> 1 == returns the first occurrence of the element
print(mytuple.index("p", 2))  # --> 2 == we specify the position we start with

"""Conversion to other data type"""
mytuple = ("a", "p", "p", "l", "e")
mylist = list(mytuple)
mytuple = tuple(mylist)
print(mylist)  # --> ['a', 'p', 'p', 'l', 'e']
print(mytuple)  # --> ('a', 'p', 'p', 'l', 'e')

mystring = "".join(mytuple)
print(mystring)  # --> apple
mytuple = tuple(mystring.split())
print(mytuple)  # --> ('apple',)

"""Converting string into tuple"""
# Python3 code to demonstrate working of
# Convert String to Tuple
# using map() + tuple() + int + split()

# initialize string
test_str = "1, -5, 4, 6, 7"

# printing original string
print("The original string : " + str(test_str))  # --> The original string : 1, -5, 4, 6, 7

# Convert String to Tuple
# using map() + tuple() + int + split()
res = tuple(map(int, test_str.split(', ')))

# printing result
print("Tuple after getting conversion from String : " + str(res))

# Python3 code to demonstrate working of
# Convert String to Tuple
# Using eval()

# initialize string
test_str = "1, -5, 4, 6, 7"

# printing original string
print("The original string : " + str(test_str))  # --> The original string : 1, -5, 4, 6, 7

# Convert String to Tuple
# Using eval()
res = eval(test_str)

# printing result
print("Tuple after getting conversion from String : " + str(res))

t = "1, -5, 4, 6, 7"
print("The original string :", end=' ')
print(t)
s = t.split(", ")
x = [int(i) for i in s]
print("Tuple after getting conversion from String :", end=' ')
print(tuple(x))

"""Slicing"""
mytuple = (1, 2, 3, 4, 5, 6, 7, 8)
slice = mytuple[3:6]
print(slice)  # --> (4, 5, 6)
slice = mytuple[1::2]
print(slice)  # --> (2, 4, 6, 8)
slice = mytuple[::-1]
print(slice)  # --> (8, 7, 6, 5, 4, 3, 2, 1) == reversing a tuple

"""Unpacking a tuple"""
mytuple = "Max", 28, "Boston"

name, age, city = mytuple  # number must match the number of elements in tuple
print(name, age, city)  # --> Max 28 Boston

"""Unpacking multiple elements with star"""
mytuple = (1, 2, 3, 4, 5, 6)
i1, *i2, i3 = mytuple
print(i1, i2, i3)  # --> 1 [2, 3, 4, 5] 6 == prints out 3 elements

"""Comparing tuple (more efficient) and list"""
import sys

mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes")  # --> 120 bytes
print(sys.getsizeof(mytuple), "bytes")  # --> 80 bytes

import timeit
# we use statement and repeat it specific number of times
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))  # --> 0.0403322
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))  # --> 0.005574400000000007

