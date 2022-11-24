# Lambda - a small one line function, that is defined without a name
# Lambda arguments: expression

add10 = lambda x: x + 10  # function with 1 argument, adds it to 10 and returns a result
print(add10)  # --> <function <lambda> at 0x0000027CBDE31160>
print(add10(5))  # --> 15

"""can take multiple arguments"""
mult = lambda x, y: x * 2 + y / 2
print(mult(2, 4))  # --> 6.0

# lambda functions usually used when you need to use it only once in a code or
# as an argument of higher order functions, meaning functions that take in other functions as arguments
# they are used along with the built-in functions - sorted(), filter() and reduce()

"""sorted"""
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]  # a list with tuples of 2 elements
# sorted by "x" index by default
points2D_sorted = sorted(points2D)  # by default, it sorts by the first argument
print(points2D)  # --> [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D_sorted)  # --> [(1, 2), (5, -1), (10, 4), (15, 1)]

# we can sort it by "y" index
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted)  # --> [(5, -1), (15, 1), (1, 2), (10, 4)]


# we can do the sam but in a longer way using another function
def sort_by_y(x):
    return x[1]


points2D_sorted = sorted(points2D, key=sort_by_y)
print(points2D_sorted)  # --> [(5, -1), (15, 1), (1, 2), (10, 4)]

"""sorting by sum of 2 elements"""
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
sum = sorted(points2D, key=lambda x: x[0] + x[1])
print(sum)  # --> [(1, 2), (5, -1), (10, 4), (15, 1)]

"""map() function - transforms each element with a function"""
# map(func, seq(for exmp a list))
a = [1, 2, 3, 4, 5]
b = map(lambda x: x * 2, a)
print(list(b))  # --> [2, 4, 6, 8, 10]

# the same we can achieve with list comprehension
a = [1, 2, 3, 4, 5]
b = [x * 2 for x in a]
print(b)  # --> [2, 4, 6, 8, 10]

"""filter()"""
# filter(func, seq) - this function returns True or False. Returns all elements to which the function evaluates the True

a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x > 3, a)  # checking what elements are bigger than 3 and return them
print(list(b))  # --> [4, 5, 6]

# checking even numbers
b = filter(lambda x: x % 2 == 0, a)
print(list(b))  # --> [2, 4, 6]

# the same thing with list comprehension
b = [x % 2 == 0 for x in a]
print(b)  # --> [False, True, False, True, False, True]
b = [x for x in a if x % 2 == 0]
print(b)  # --> [2, 4, 6]

"""reduce function"""
# reduce(func, seq) - it repeatedly applies a function to the elements and returns a single value
# reduce() function always take 2 arguments
# since python 3 we have to import it
from functools import reduce

a = [1, 2, 3, 4, 5, 6]

product_a = reduce(lambda x, y: x * y, a)
print(product_a)  # --> 720
