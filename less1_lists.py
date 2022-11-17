# Lists: ordered, mutable, allows duplicate elements

"""Creating a list"""
mylist = ["banana", "cherry", "apple"]  # inside we put any elements, separated with comma
print(mylist)  # --> ['banana', 'cherry', 'apple']

mylist2 = list()  # creating an empty list
print(mylist2)  # --> []

"""List can contain different data types with its duplicates"""
mylist = [4, True, "string", 4]  # [4, True, 'string', 4]
print(mylist)

"""Accessing elements of the list via referring to its index """
mylist = ["banana", "cherry", "apple"]
item = mylist[0]
print(item)  # --> banana

item1 = mylist[-2]  # --> cherry
print(item1)

"""iteration through a list"""
mylist = ["banana", "cherry", "apple"]
for i in mylist:
    print(i, mylist.index(i))  # --> banana 0, cherry 1, apple 2

"""checking if an item is inside our list"""
if "orange" in mylist:
    print("yes")
else:
    print("no")  # --> no

"""Check how many elements we have inside our list"""
print(len(mylist))  # --> 3

"""Other list methods"""
mylist.append("orange")
print(mylist)  # --> ['banana', 'cherry', 'apple', 'orange'] at the end of the list

mylist.insert(0, "lemon")  # we have to specify an index where to insert an item
print(mylist)  # --> ['lemon', 'banana', 'cherry', 'apple', 'orange']

"""pop method returns and also removes the last item"""
item = mylist.pop()
print(item)  # --> orange
print(mylist)  # --> ['lemon', 'banana', 'cherry', 'apple']

"""remove specific element"""
item = mylist.remove("cherry")  # function remove() doesn't return anything but None
print(mylist)  # --> ['lemon', 'banana', 'apple']

item = mylist.clear()  # removes all elements of the list
print(mylist)  # --> []

"""reverse or sort a list with reverse()/sort() methods"""
mylist = ["banana", "cherry", "apple"]
mylist.reverse()
print(mylist)  # --> ['apple', 'cherry', 'banana']

mylist.sort()
print(mylist)  # --> ['apple', 'banana', 'cherry'] ascending order

"""another way to reverse a list"""
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
slice = mylist[::-1]  # reverses our list
print(slice)  # --> [8, 7, 6, 5, 4, 3, 2, 1]

"""if we don`t want to change our original list but apply changes to another one"""
mylist = [1, -3, 5, 0, 13, 2]
mylist2 = sorted(mylist)
print(mylist)  # --> [1, -3, 5, 0, 13, 2]
print(mylist2)  # --> [-3, 0, 1, 2, 5, 13]

"""creating a new list with the same elements multiple times"""
mylist = [1, 2, 3, 4]
new_list = mylist * 3
print(new_list)  # --> [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

"""connection of 2 list"""
mylist = [1, 2, 3]
mylist2 = [4, 5, 6]
new_list = mylist + mylist2
print(new_list)  # --> [1, 2, 3, 4, 5, 6]

"""slicing a very nice way to access sub parts of our list"""
mylist = [1, 2, 3, 4, 5]
slice = mylist[1:3]
print(slice)  # --> [2, 3]

"""using a step index"""
mylist = [1, 2, 3, 4, 5, 6, 7, 8]
slice = mylist[::2]  # picks every second item of the list
print(slice)  # --> [1, 3, 5, 7]

"""copying a list"""
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org.copy()  # copies original list and later modification of copy won't affect the original
list_cpy1 = list_cpy

list_cpy.append("lemon")
print(list_org)  # --> ['banana', 'cherry', 'apple'] unaffected with changes of copy
print(list_cpy)  # --> ['banana', 'cherry', 'apple', 'lemon']
print(list_cpy1)  # --> ['banana', 'cherry', 'apple', 'lemon'] keeps changes

"""other ways of copying"""
list_org = ["banana", "cherry", "apple"]
list_cpy = list(list_org)
list_cpy1 = list_org[:]
list_cpy.append("mango")
list_cpy1.append("strawberry")

print(list_org)  # --> ['banana', 'cherry', 'apple']
print(list_cpy)  # --> ['banana', 'cherry', 'apple', 'mango']
print(list_cpy1)  # --> ['banana', 'cherry', 'apple', 'strawberry']

"""List comprehension - an elegant way to create a new list from existing with 1 line"""
a = [1, 2, 3, 4, 5, 6]
b = [i * i for i in a]
print(b)  # --> [1, 4, 9, 16, 25, 36]


