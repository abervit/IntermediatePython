# Strings (collection data type) - ordered, immutable, text representation

"""Creating a string"""
my_string = "Hello world"  # or we can use single quotes
print(my_string)  # --> Hello world

my_string = 'I\'m a programmer'
print(my_string)  # --> I'm a programmer

"""Triple quotes mainly are used for multiple lines code or comments"""
my_string = """Hello
World"""
print(my_string)  # --> Hello (another line) World

my_string = """Hello \
World"""  # \ will cancel the new line and continue with current
print(my_string)  # --> Hello World

"""Accessing the characters od sub-strings with indexing"""
my_string = "Hello World"
char = my_string[0]
print(char)  # --> H
char = my_string[-2]
print(char)  # --> l

"""We can't change the characters of the list, because it's immutable"""
my_string = "Hello World"
# my_string[0] = 1  # will raise an error
print(my_string)  # --> TypeError: 'str' object does not support item assignment

try:
    my_string[1] = "Hello again"
except TypeError as te:
    print("String doesn't support an item assignment")  # --> String doesn't support an item assignment

"""Slicing"""
my_string = "Hello World"
sub_string = my_string[0:5]
print(sub_string)  # --> Hello

"""Reversing a string with slicing"""
my_string = "Hello World"
rev_string = my_string[::-1]
print(rev_string)  # --> dlroW olleH

"""Concatenation strings"""
greeting = "Hello ,"
name = "Tom. "
wish = "Have a good day!"
text = greeting + name + wish
print(text)  # --> Hello ,Tom. Have a good day!

"""Iteration through a string"""
my_string = "Hello"
for i in my_string:
    print(i)  # --> prints out each character of "Hello"

"""Checking if character or substring is inside our string"""
my_string = "Hello World"
if "a" in my_string:
    print("yes")
else:
    print("no")  # --> no

if "orl" in my_string:
    print("yes")  # --> yes
else:
    print("no")

"""String with some wide spaces"""
my_string = "    Hello World   "
print(my_string)  # -->     Hello World
# if we want to get rid of wide spaces
my_string = my_string.strip()  # removes wide spaces. it doesn't change the original string
print(my_string)  # --> Hello World

"""Upper case etc."""
my_string = "hello world"
print(my_string.upper())  # --> HELLO WORLD
print(my_string.lower())  # --> hello world
print(my_string.capitalize())  # --> Hello world

print(my_string.startswith("Hel"))  # --> False == capitalized  "H"
print(my_string.startswith("Hel".lower()))  # --> True
print(my_string.endswith("orld"))  # --> True

"""Finding an index of character  or substring"""
my_string = "hello world"
print(my_string.index("hello"))  # --> 0 == index of the first character of substring

print(my_string.index("l"))  # --> 2 == index of the first occurrence of character if we have more of them in the string
print(my_string.index("l", 5))  # --> 9 == we pass an index to start finding with, from 9th index to search

print(my_string.find("o"))  # --> 4 == finds an index of the character, first occurrence
print(my_string.find("rx"))  # --> -1 == returns -1 when an index of substring is not find

"""Counting"""
my_string = "hello world"
print(my_string.count("o"))  # --> 2
print(my_string.count("ll"))  # --> 1

"""Replacing characters or substrings in our string"""
my_string = "hello world"
print(my_string.replace("world", "Tom"))  # --> hello Tom
print(my_string.replace("o", "a"))  # --> hella warld

"""Lists and strings"""
my_string = "How are you doing"
my_list = my_string.split(
    " ")  # converting a string into a list, by default the limiter is pace. It looks for each space
print(my_list)  # --> ['How', 'are', 'you', 'doing']

new_string = " ".join(my_list)
print(new_string)  # --> How are you doing

from timeit import default_timer as timer

my_list = ["a"] * 6
print(my_list)  # --> ['a', 'a', 'a', 'a', 'a', 'a']
my_string = ""
# this is bad code
start = timer()
for i in my_list:
    my_string += i
stop = timer()
time = stop - start
print(my_string, time)  # --> aaaaaa 1.4000000000055635e-06

# good - much cleaner and much faster
start = timer()
my_string = "".join(my_list)
stop = timer()
time = stop - start
print(my_string, time)  # --> aaaaaa 5.999999999964367e-07

"""Formatting strings - %, .format(), f-strings"""

var = "Tom"  # %s - string, %d - number (integer, decimal), %f - floating (by default 6 digits after point)
my_string = "The variable is %s" % var
print(my_string)  # --> The variable is Tom

var = 2
my_string = "The variable is %d" % var  # for numbers, converts floats into integers
print(my_string)  # --> The variable is 2

var = 2.34343423
my_string = "the variable is %f" % var
print(my_string)  # --> the variable is 2.343434

my_string = "the variable is %.2f" % var  # we specify the number of digits after floating point
print(my_string)  # --> the variable is 2.34

var = 2.34343423
my_string = "the variable is {:.2f}".format(var)  # we specify how many digits we want - 2
print(my_string)  # --> the variable is 2.34

greet = "Helo"
name = "Tom"
age = 23
my_string = "{}, {}. You are {} years old, if I'm correct.".format(greet, name, age)
print(my_string)  # --> Helo, Tom. You are 23 years old, if I'm correct.

# we have to be careful about order of variables when we pass them
my_string = "{}, {}. You are {} years old, if I'm correct.".format(age, greet, name)
print(my_string)  # --> 23, Helo. You are Tom years old, if I'm correct.

# the best way is with f-strings - easy to read, faster
greet = "Helo"
name = "Tom"
age = 23
my_string = f"{greet}, {name}. You are {age} years old, if I'm correct."
print(my_string)  # --> Helo, Tom. You are 23 years old, if I'm correct.

my_string = f"{greet.upper()}, {name.replace('om', 'amara')}. You are {age * 2} years old, if I'm correct."
print(my_string)  # --> HELO, Tamara. You are 46 years old, if I'm correct.

question_promot = ["What color are bananas?\n(a) yellow\n(b) red\n(c) green\n\n",
                   "What color are apples?\n(a) black\n(b) red/yellow\n(c) blue\n\n",
                   "What color are oranges?\n(a) green\n(b) pink\n(c) orange\n\n"
                   ]


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [Question(question_promot[0], "a"),
             Question(question_promot[1], "b"),
             Question(question_promot[2], "c")]


def game(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You answered {score} of 3 correct!")


game(questions)
