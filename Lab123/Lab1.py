# Example 1: Print "Hello, World!"
print("Hello, World!")

# Example 2: Python Indentation
if 5 > 2:
    print("Five is greater than two!")

# Example 3: Python Variables
x = 5
y = "Hello, World!"
print(x)
print(y)

# Example 4: Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Example 5: Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

# Example 6: Single or Double Quotes
x = "John"
x = 'John'

# Example 7: Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a

# Example 8: Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Example 9: Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Example 10: One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Example 11: Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Example 12: Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Example 13: Output Variables with +
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Example 14: Global Variables
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# Example 15: Global Variables Inside a Function
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)

# Example 16: Data Types
x = 5
print(type(x))
x = "Hello World"
print(type(x))
x = 20.5
print(type(x))
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("apple", "banana", "cherry")
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
x = True
print(type(x))
x = b"Hello"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = None
print(type(x))

# Example 17: Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# Example 18: Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Example 19: Random Number
import random

print(random.randrange(1, 10))

# Example 20: Strings
a = "Hello"
print(a)

# Example 21: Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Example 22: Strings are Arrays
a = "Hello, World!"
print(a[1])

# Example 23: Looping Through a String
for x in "banana":
    print(x)

# Example 24: String Length
a = "Hello, World!"
print(len(a))

# Example 25: Check String
txt = "The best things in life are free!"
print("free" in txt)

# Example 26: Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

# Example 27: Slicing Strings
b = "Hello, World!"
print(b[2:5])

# Example 28: Slice From the Start
b = "Hello, World!"
print(b[:5])

# Example 29: Slice To the End
b = "Hello, World!"
print(b[2:])

# Example 30: Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# Example 31: Modify Strings
a = "Hello, World!"
print(a.upper())

# Example 32: Modify Strings
a = "Hello, World!"
print(a.lower())

# Example 33: Remove Whitespace
a = " Hello, World! "
print(a.strip())

# Example 34: Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Example 35: Split String
a = "Hello, World!"
print(a.split(","))

# Example 36: String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Example 37: String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Example 38: Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Example 39: String Methods
a = "Hello, World!"
print(a.capitalize())
print(a.casefold())
print(a.center(20))
print(a.count("l"))
print(a.encode())
print(a.endswith("!"))
print(a.expandtabs(2))
print(a.find("o"))
print(a.format())
print(a.format_map({}))
print(a.index("o"))
print(a.isalnum())
print(a.isalpha())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())
print(a.islower())
print(a.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.isupper())
print(a.join(["Hello", "World"]))
print(a.ljust(20))
print(a.lower())
print(a.lstrip())
print(a.maketrans("H", "J"))
print(a.partition("o"))
print(a.replace("H", "J"))
print(a.rfind("o"))
print(a.rindex("o"))
print(a.rjust(20))
print(a.rsplit(","))
print(a.rstrip())
print(a.split(","))
print(a.splitlines())
print(a.startswith("H"))
print(a.strip())
print(a.swapcase())
print(a.title())
print(a.translate(a.maketrans("H", "J")))
print(a.upper())
print(a.zfill(20))