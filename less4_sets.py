# Sets (collection data type) that is unordered, mutable, no duplicates

"""Creation"""
myset = {1, 2, 3, 1, 2}
print(myset)  # --> {1, 2, 3}

myset = set([1, 2, 3, 4])
print(myset)  # --> {1, 2, 3, 4}
"""With set we can find out how many characters we have in a word"""
myset = set("hello")
print(myset)  # --> {'l', 'o', 'h', 'e'}

myset = set()  # --> empty set
print(type(myset))  # --> <class 'set'>
myset = {}  # --> empty dictionary
print(type(myset))  # --> <class 'dict'>

"""Adding new elements"""
myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)  # --> {1, 2, 3}

"""Removing elements. If an element is not in the set we'll get an error"""
myset = {1, 2, 3, 1, 2}
myset.remove(3)
print(myset)  # --> {1, 2}

"""Another remove method is discard - if the element is not find, nothing will happen"""
myset = {1, 2, 3, 1, 2}
myset.discard(5)
print(myset)  # --> {1, 2, 3}

myset.clear()  # --> will clear a whole set
myset = {1, 2, 3, 1, 2}
print(myset.pop())  # --> 1 == removes and returns the last value of the set
print(myset)  # --> {2, 3}

"""Iteration through a set with for loop"""
for i in myset:  # iterates through all elements
    print(i)

"""Checking if an element is inside our set"""
if 10 in myset:
    print("yes")
else:
    print("no")  # --> no

"""Union and intersection"""
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

"""Union combines elements from both sides without duplication"""
union = odds.union(evens)
print(union)  # --> {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

"""Intersection of 2 sets"""
inter = odds.intersection(evens)
print(inter)  # --> set() == empty set - only elements that are in both sets at the same time

inter = odds.intersection(primes)
print(inter)  # --> {3, 5, 7}

"""Difference of 2 sets - returns elements of the first set that are not in the second"""
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
differ = setA.difference(setB)
print(differ)  # --> {4, 5, 6, 7, 8, 9}
differ = setB.difference(setA)
print(differ)  # --> {10, 11, 12}

# symmetric difference method
differ = setA.symmetric_difference(setB)  # returns different elements from both sets
print(differ)  # --> {4, 5, 6, 7, 8, 9, 10, 11, 12}
differ = setB.symmetric_difference(setA)
print(differ)  # --> {4, 5, 6, 7, 8, 9, 10, 11, 12}

# difference and symmetric_difference methods won't modify the original sets,
# but we can also modify our sets in plays
"""update() method"""
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.update(setB)  # --> keeps elements from both sets
print(setA)  # --> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

"""intersection_update() method"""
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)  # --> keeps only similar elements from both sets
print(setA)  # --> {1, 2, 3}

"""difference_update() method"""
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)  # returns only different elements from first set
print(setA)  # --> {4, 5, 6, 7, 8, 9}

"""symmetric_difference_update() method"""
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)  # updates with different elements from both sets
print(setA)  # --> {4, 5, 6, 7, 8, 9, 10, 11, 12}

"""sub sets and super sets and disjoint"""
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
print(setA.issubset(setB))  # --> False == all elements of first set are not in the second

print(setA.issuperset(setB))  # --> True == all elements of second set are in the first

# returns True if both sets don't have the same elements
print(setA.isdisjoint(setB))  # --> False == have the same elements
print(setA.isdisjoint(setC))  # --> True

"""Copying 2 sets"""
setA = {1, 2, 3, 4, 5, 6}
setB = setA  # when we modify a copy it affects the original one
setB = setA.copy()
print(setB)  # --> {1, 2, 3, 4, 5, 6}
setB = set(setA)
print(setB)  # --> {1, 2, 3, 4, 5, 6}

"""The frozen set - collection data type, the same as set() but immutable"""
"""You can't change after its creation"""
set = frozenset([1, 2, 3, 4, 5])  # we pass only 1 element which is iterable
print(set)  # --> {1, 2, 3, 4, 5}
set.add(23)
print(set)  # --> AttributeError: 'frozenset' object has no attribute 'add'
