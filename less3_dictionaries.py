# Dictionaries (collection data-type) - key-values pairs, unordered and mutable

"""Creating dictionary"""
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)  # --> {'name': 'Max', 'age': 28, 'city': 'New York'}

mydict = dict(name="Max", age=28, city="New York")  # we don't have to use quotes for the keys
print(mydict)  # --> {'name': 'Max', 'age': 28, 'city': 'New York'}

"""Accessing the value"""
value = mydict["name"]
print(value)  # --> Max

# value = mydict["surname"]
# print(value)  # --> KeyError: 'surname' == not in the dictionary

"""Dictionary is mutable, so we can change or add items after its creation"""
mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict["email"] = "max@pt.com"
print(mydict)  # --> {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@pt.com'}

"""if the key already exists, it will be overriden"""
mydict["email"] = "max.new@pt.com"
print(mydict)  # --> {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max.new@pt.com'}

"""Deleting items from dictionary"""
del mydict["email"]
print(mydict)  # --> {'name': 'Max', 'age': 28, 'city': 'New York'}

mydict.pop("age")
print(mydict)  # --> {'name': 'Max', 'city': 'New York'}

mydict.popitem()  # --> removes the last inserted item
print(mydict)  # --> {'name': 'Max'}

"""Check if the key is in dictionary - 2 common ways"""
mydict = {"name": "Max", "age": 28, "city": "New York"}
if "name" in mydict:
    print("yes, it is")  # --> yes, it is
else:
    print("no, not this time")

try:
    print(mydict["name"])  # --> Max
except:
    print("error")

"""Looping through the dictionary"""
for key in mydict:
    print(key)  # --> prints out all the keys

for key in mydict.keys():
    print(key)  # --> prints out all the keys

for value in mydict.values():
    print(value)  # --> prints out all the values

for key, value in mydict.items():
    print(key, value)  # --> prints out key-value pairs

"""Copying the dictionary"""
mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict_cpy = mydict  # if we modify the copy it will also modify the original one
mydict_cpy["email"] = "max@ws.sd"
print(mydict)  # --> {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@ws.sd'}
print(mydict_cpy)  # --> {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@ws.sd'}

mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict_cpy = mydict.copy()  # or we can use dict(mydict)
mydict_cpy["email"] = "max@ws.sd"
print(mydict)  # --> {'name': 'Max', 'age': 28, 'city': 'New York'}
print(mydict_cpy)  # --> {'name': 'Max', 'age': 28, 'city': 'New York', 'email': 'max@ws.sd'}

"""Merging 2 dictionaries, appending"""
mydict1 = {"name": "Max", "age": 28, "city": "New York"}
mydict2 = {"name": "Tom", "age": 13, "city": "New York"}
mydict1.update(mydict2)  # --> updates the existing one with new information if it's different
print(mydict1)  # --> {'name': 'Tom', 'age': 13, 'city': 'New York'}

"""As keys - we can use any immutable type - numbers, or even a tuple if it contains immutable elements"""
mydict = {3: 9, 6: 36, 9: 81}
print(mydict)  # --> {3: 9, 6: 36, 9: 81}

mytuple = (3, 5)
mydict = {mytuple: 8}
print(mydict)  # --> {(3, 5): 8}

mylist = [3, 5]
mydict = {mylist, 8}  # list is mutable so we can't use it as a key for dictionary
print(mydict)  # --> TypeError: unhashable type: 'list'

"""When we try o get a value by key index we have to use key-mane, not actual index"""
mydict = {3: 9, 6: 36, 9: 81}
# print(mydict[0])  # --> KeyError: 0

print(mydict[6])  # --> 36

