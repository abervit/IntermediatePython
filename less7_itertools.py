# Itertools (collection of tools for handling iterators) - the data type that can be used in for loop.
# The most common iterator is a list. Itertools offer some advanced tools
# Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators
# Functions creating iterators for efficient looping -- link below
# https://docs.python.org/3/library/itertools.html

"""product"""
from itertools import product

a = [1, 2]
b = [3, 4]
prod = product(a, b)  # computes Cartesian product of the input iterables
print(prod)  # --> <itertools.product object at 0x000002131B0951C0>
print(list(prod))  # --> [(1, 3), (1, 4), (2, 3), (2, 4)]

# defining a number of repetitions
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)  # we set number of repeats
print(list(prod))  # --> [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

"""permutations"""
from itertools import permutations

# permutations will return all possible orderings of an input

a = [1, 2, 3]
perm = permutations(a)
print(perm)  # <itertools.permutations object at 0x000001B0186D5B30>
print(list(perm))  # --> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# we can specify the length of permutations if we want to have it shorter
a = [1, 2, 3]
perm = permutations(a, 2)  # 2 is an argument of length
print(list(perm))  # --> [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

"""combinations"""
from itertools import combinations

# combinations will make all possible combinations with specified length
# we don't have combinations of the same argument - no repetitions here
a = [1, 2, 3, 4]
comb = combinations(a, 2)  # 2 - required argument for length
print(comb)  # <itertools.combinations object at 0x000001C0D5D35A90>
print(list(comb))  # --> [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# if we want repetitions of the same argument we use combinations with replacement function
from itertools import combinations, combinations_with_replacement

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))  # --> [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

"""accumulate"""
# accumulate function makes an iterator that returns accumulated sums or any other binary function that we want
# to give as an input
from itertools import accumulate

a = [1, 2, 3, 4]
accum = accumulate(a)
print(a)  # --> [1, 2, 3, 4]
print(accum)  # --> <itertools.accumulate object at 0x0000026430162440>
print(list(accum))  # --> [1, 3, 6, 10] == accumulated sums of our list

# by default, it computes a sum, but we can multiply the elements
from itertools import accumulate
import operator

a = [1, 2, 3, 4]
accum = accumulate(a, func=operator.mul)
print(a)  # --> [1, 2, 3, 4]
print(list(accum))  # --> [1, 2, 6, 24]
accum = accumulate(a, func=operator.truediv)
print(list(accum))  # --> [1, 0.5, 0.16666666666666666, 0.041666666666666664]
a = [1, 2, 5, 3, 4, 6]
accum = accumulate(a, func=max)
print(a)  # --> [1, 2, 5, 3, 4, 6]
print(list(accum))  # --> [1, 2, 5, 5, 5, 6]
accum = accumulate(a, func=min)
print(a)  # --> [1, 2, 5, 3, 4, 6]
print(list(accum))  # --> [1, 1, 1, 1, 1, 1]

"""groupby"""
from itertools import groupby


# the groupby function makes an iterator that returns keys and groups from an iterable

def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a,
                    key=smaller_than_3)  # we group our list into other list comparing if it's smaller than 3 using a function
print(group_obj)  # --> <itertools.groupby object at 0x000002D922BE5CC0>
print(list(
    group_obj))  # --> [(True, <itertools._grouper object at 0x000002747D3E7BB0>), (False, <itertools._grouper object at 0x000002747D3E7B80>)]

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))  # -->True [1, 2] False [3, 4] == 1 and 2 are smaller than 3 so it's True

"""lambda"""


# lambda - small one line function that can have an input and will return an output
def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))  # -->True [1, 2] False [3, 4]

persons = [{"name": "Tim", "age": 23}, {"name": "Bob", "age": 23},
           {"name": "Mike", "age": 54}, {"name": "Anna", "age": 13}]

group_obj = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))

# results from above:
# 23 [{'name': 'Tim', 'age': 23}, {'name': 'Bob', 'age': 23}]
# 54 [{'name': 'Mike', 'age': 54}]
# 13 [{'name': 'Anna', 'age': 13}]

"""infinite operators"""
from itertools import count, cycle, repeat

for i in count(10):
    print(i)  # makes an infinite function which starts with 10, if only we won't stop it
    if i == 15:
        break

# cycle() will cycle infinetely through an iterable
a = [1, 2, 3]

# for i in cycle(a):
#     print(i)

# repeat method
a = [1, 2, 3]
for i in repeat(a, 4):  # 4 -second argument, means we want to repeat "a" 4 times
    print(i)