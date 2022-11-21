# Collections (special container data types) provides some additional functionality compareto regular data containers
# Collections : Counter, namedtuple, OrderedDict, defaultdict, deque

"""Counter - container that stores elements as dictionary keys and their counts as dictionary values."""
import collections
from collections import Counter

a = "aaaabbbbbbccccc"
my_counter = Counter(a)  # returns all different characters as keys and their count as values
print(my_counter)  # --> Counter({'b': 6, 'c': 5, 'a': 4})

print(my_counter.items())  # --> dict_items([('a', 4), ('b', 6), ('c', 5)])
print(my_counter.keys())  # --> dict_keys(['a', 'b', 'c'])
print(my_counter.values())  # --> dict_values([4, 6, 5])

# checking the most common element in our counter dictionary

a = "12111112332332453456345"
# TypeError: 'int' object is not iterable == it means you are trying to loop through an integer or other data type that loops cannot work on
my_counter = Counter(a)
print(my_counter.most_common())  # --> [('1', 6), ('3', 6), ('2', 4), ('4', 3), ('5', 3), ('6', 1)]
print(my_counter.most_common(1))  # --> [('1', 6)] == returns list of tuple 1 the most common element
print(my_counter.most_common(2))  # --> [('1', 6), ('3', 6)] == 2 the most common elements
print(my_counter.most_common(2)[1][1])  # --> 6

# we can also have a list with all different elements
a = "112323453634"
my_counter = Counter(a)
print(my_counter.elements())  # --> <itertools.chain object at 0x000002B4C404FFA0>
print(list(my_counter.elements()))  # --> ['1', '1', '2', '2', '3', '3', '3', '3', '4', '4', '5', '6']

print(tuple(my_counter.elements()))  # --> ('1', '1', '2', '2', '3', '3', '3', '3', '4', '4', '5', '6')

print(set(my_counter.elements()))  # --> {'4', '6', '3', '1', '5', '2'}

"""namedtuple - an easy way to create a lightweight object type sim ilar to a struct"""
from collections import namedtuple

# First we have to define a name for tuple. As first argument we give a class name,
# which usually is the same as tuple's name. As a second argument we use all the different fields we want separated by comma or space

Point = namedtuple("Point", "x, y")
point1 = Point(1, -3)
print(point1)  # --> Point(x=1, y=-3)
print(point1.x, point1.y)  # --> 1 -3

print(point1.index(1))  # --> 0 == the index of 1 is 0

"""OrderedDict - like ordinary dictionary but they remember the order of items they were inserted"""
"""Since python 3.7 regular dictionary also can remember the order of items"""
from collections import OrderedDict

ordered_dit = OrderedDict()
ordered_dit["b"] = 2
ordered_dit["c"] = 3
ordered_dit["d"] = 4
ordered_dit["e"] = 5
ordered_dit["a"] = 1
print(ordered_dit)  # --> OrderedDict([('b', 2), ('c', 3), ('d', 4), ('e', 5), ('a', 1)])

# in python 3.7
ordered_dit = {}
ordered_dit["b"] = 2
ordered_dit["c"] = 3
ordered_dit["d"] = 4
ordered_dit["e"] = 5
ordered_dit["a"] = 1
print(ordered_dit)  # --> {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'a': 1} == still remember an order

"""defaultdict - similar to a usual dictionary container with the only difference it will have a default value of a key it hasn't been set yet"""

from collections import defaultdict

# as an argument we'll give a default type for exm - int
default_dict = defaultdict(int)  # float, list etc
default_dict['a'] = 1
default_dict["b"] = 2
print(default_dict)  # --> defaultdict(<class 'int'>, {'a': 1, 'b': 2})
print(default_dict["a"])  # --> 1

# if we put a key that doesn't exist it will return 0
print(default_dict["c"])  # --> 0

"""deque - is double ended queue and it can be used to add or remove elements from both ends"""
"""it;s very efficient"""
from collections import deque

deq = deque()
deq.append(1)
deq.append(2)
print(deq)  # --> deque([1, 2])
deq.appendleft(0)
deq.appendleft(-1)
print(deq)  # --> deque([-1, 0, 1, 2])

deq.pop()  # removes an element from the right - the last one
print(deq)  # --> deque([-1, 0, 1])

deq.popleft()  # --> removes the first element from the left
print(deq)  # --> deque([0, 1])

deq.extend([2, 3, 4])  # with multiple elements
print(deq)  # --> deque([0, 1, 2, 3, 4])

deq.extendleft([-1, -2, -3])
print(deq)  # --> deque([-3, -2, -1, 0, 1, 2, 3, 4])

deq.rotate(1)  # rotates all elements by 1 place - the last element moves to first
print(deq)  # --> deque([4, -3, -2, -1, 0, 1, 2, 3])

deq.rotate((-2))  # rotates to the left
print(deq)  # --> deque([-2, -1, 0, 1, 2, 3, 4, -3])
