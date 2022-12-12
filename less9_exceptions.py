# Errors and exceptions
# Difference between syntax error and an exception

# Errors

"""Syntax error -->  SyntaxError: invalid syntax"""
# a = 5 print(a)


"""Exception error --> TypeError: unsupported operand type(s) for +: 'int' and 'str'"""
# a = 5 + "5"
# print(a)

"""Exception error --> ModuleNotFoundError: No module named 'something'"""
# import something

"""Exception error --> NameError: name 'c' is not defined"""
# a = 5
# b = c

"""Exception error --> FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'"""
# f = open("file.txt")

"""Exception error --> ValueError: list.remove(x): x not in list"""
# a = [1, 2, 3]
# a.remove(5)
# print(a)

"""Exception error --> IndexError: list index out of range"""
# a = [1, 2, 3]
# print(a[4])

"""Exception error --> KeyError: 'surname' """
# dict = dict(name="Tom")
# print(dict["surname"])

"""Raising an exceptions"""
# x = -5
# if x < 0:
#     raise Exception("x should be positive")  # --> Exception: x should be positive

"""Assertion error - will throw an assertion error if our condition is not True"""
x = -5
# assert (x >= 0)  # --> Exception: x should be positive
# assert (x >= 0), "Should be bigger than 0"  # --> AssertionError: Should be bigger than 0


"""Handling exceptions"""
try:
    a = 5 / 0
    b = "a" + a
except ZeroDivisionError as div:
    print(div)  # --> division by zero
except TypeError as typ:
    print(typ)  # --> can only concatenate str (not "float") to str
else:
    print("Everything is ok")
finally:  # runs always to make some cleaning operations
    print("Cleaning up...")  # --> Cleaning up...


# Typically, we add Error to a class Error
class ValueTooHighError(Exception):
    pass


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")


# test_value(200)  # --> __main__.ValueToHighError: value is too high

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)  # --> value is too high


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 10:
        raise ValueTooSmallError("value too small", x)  # We pass first message and then a value


try:
    test_value(8)
except ValueTooHighError as e:
    print(ValueTooHighError)
except ValueTooSmallError as e:
    print(e.message, e.value)  # --> value too small 8
