import math

print("Getting Started")
print()
# First Example
x = 23
print(x)

# Second Example
x = 40
print(x)

# Third Example
request = "I want to learn python "
print("What stack you want to learn? " + request)
print()
print("String Examples:")
# String variables

string1 = "Grapes and olives."
string2 = " --also, I have 5 apples"
# Select a specific Portion of a string (The values within [] represent the characters within the variable)

piece = string1[0:6]
print("Piece:", piece)

# Combine two strings and print to the new string with a new variable
longer_string = piece + string2
print("Longer_string:", longer_string)

# Print a Blank Line
print()

# Integer Variables
print("Integer Examples")
x1 = 7
x2 = 993
# New variable storing result of adding two integers
x3 = x1 + x2
print("x3:", x1+x2)
# Reassign variable to the result from floating point division
x3 = x1/3
print("x3:", x3)
# Reassign variable to the result from floating point division
x3 = x1//3
print("x3:", x3)

# Float Variables
print()
print("Float Examples")
float1 = 3.14
float2 = 5.0

# Subtract two Floats and point to that value with a new variable
subtraction = float2 - float1
print("Subtraction:", subtraction)

# Create and Int from a flot; Ignores decimal portion - does not round)
float_to_int = int(3.14)
float_to_int2 = int(3.94)
print("float_to_int:", float_to_int)
print("float_to_int:", float_to_int)

# Create an int from a float by rounding value to Nearest Integer
float_rounded1 = round(3.14)
float_rounded2 = round(3.94)
print("float_rounded1:", float_rounded1)
print("float_rounded2:", float_rounded2)
print()

# Boolean Variables
print("Boolean Examples")
fact = True
fiction = False

a = 9
b = 3
boolean1 = (a <= b)
print("Boolean1:", boolean1)

x = "Hello"
y = "Hello World"
boolean2 = (x == y[0:5])
print("Boolean2:", boolean2)

# Logical Operators
# "or" returns True if one of the statements is true
# "and" returns True if both statements are true
# "not" reverse the result - returns false if the result is true
print("or:", boolean1 or boolean2)
print("and:", boolean1 and boolean2)
print("not:", not boolean2)
print()

# List Variables
print("List Examples")
list1 = [13, 14, 15, 16, 17]
list2 = ['butterfly', 'dog', 'frog', 'tiger']

# Value at a particular index
val1 = list1[0]
print("val1:", val1)
val2 = list2[3]
print("val2:", val2)

# Another variable pointing to the same list
list3 = list1
print("list1:", list1, "and list3", list3)

# Append Value to the end of list (mutates the list)
list1.append(23)
print("list1 after append:", list1)

# Note that list3 points to the same list object, so it also changed
print("list1:", list1, "and list3", list3)

# Insert value at a particular index (mutates the list)
list2.insert(1, 'gorilla')
print("list2 after inset:", list2)

# Remove and Return Value with Pop Methods (mutates the list)
popped_val = list1.pop(0)
print("popped_val:", popped_val)
print("list1 after pop:", list1)
print()

# Tuple Variables
print("Tuple Examples:")
tup1 = (9, 8, 7, 6, 5, 9, 9)
tup2 = ('hat', 'scarf', 'sweater', 'gloves')

# Find length of Tuples
tup1_len = len(tup1)
print("tup1_len:", tup1_len)
print("len of tup2:", len(tup2))

# Find number of occurrences of a particular element
tup1_count = tup1.count(9)
print("tup1_count:", tup1_count)

# Set Variables
print()
print("Set Examples:")
set1 = {1, 1, 1, 1, 1, 1, 4, 2, 3, 4}
set2 = {'guitar', 'piano', 'trombone', 'cymbal', 'bass', 'piano', 'piano'}

# Creating sets extracts unique elements and make unordered collection
print("set1:", set1)
print("set2:", set2)

# Join two sets together
set3 = set1.union(set2)
print("set3:", set3)

# Dictionary Variables
print()
print("Dictionary Examples:")
dict1 = {
    "sports": ["football", "basketball", "baseball", "hockey"],
    "IDs": [7, 2, 3],
    "name": 'John',
    "age": 23
}

# Get values corresponding to a key
print("Value for 'sports' in dict1:", dict1.get("sports"))
print("Value for 'age' in dict1:", dict1["age"])

# Add a key-value pair to dictionary
dict1['fav_color'] = 'green'
print("dict1 with new key:", dict1)

# Extract all keys and values from dictionary
print("keys in dict1:", dict1.keys())
print("values in dict1:", dict1.values())
# Sequence of Tuples of (Key, value) in dict1
print("items in dict1:", dict1.items())

# Loop Examples
print()
list1 = ['a', 'b', 'c', 'd', 'e']
# One common way to leverage a for loop is to iterate sequentially over the elements of a data structure
print('For-Loop Method #1')
for j in list1:
    print("Next element is sequence is:", j)
# Another common way is using range and iterating through indices
print('------------')
print('For-Loop Method #2')
for i in range(len(list1)):
    print("Element at Index:", i, "is", list1[i])
print('------------')
print('While Loop')
k = 0
while k < len(list1):
    print(list1[k])
    k += 1
print()

# Exercise: Calculating Average Weight - find the average weight of a group of dogs
print("Average Weight of Group of Dogs:")
sum1 = 0
weights = [25, 37, 53, 64, 82, 91]

for weight in weights:
    sum1 += weight
avg = sum1/len(weights)
print(avg)
print()

# Conditionals
print("Conditionals:")
x = 5
if x <= 5:
    print('small')
elif 6 <= x <= 10:
    print('medium')
else:
    print('large')
print("Exercise: Find Max Organically among: [4525, 1232, 98775, 1243, 88888, 9853211, 59612]")
# Method 1
vals = [4525, 1232, 98775, 1243, 88888, 9853211, 59612]
maximum = 0
for num in vals:
    if num > maximum:
        maximum = num


print("Method1:", maximum)
# Method 2
maximum = None
for num in vals:
    if maximum is None or num > maximum:
        maximum = num
print("Method2:", maximum)

# Functions
print()
print("Functions Examples:")
# Creating a function for the Conditional example


def number_describer(x):
    if x <= 5:
        print('small')
    elif 6 <= x <= 10:
        print('medium')
    else:
        print('large')


number_describer(7)

# Variable Scope in Functions
print()
print("Variable Scope in Functions:")


def greeter():
    person = "Sabrina"
    print("Hi " + person + "!")


greeter()
# person is only written within the function, so using print(person) outside of it won't work
# now's let define the variable person out of the function
person = "Tom"


def greeter():
    print("Hi " + person + "!")


greeter()
print(person)
# You can still call a variable defined out of a function from within it
# Now let's try with different variables with the same, one within and one outside
person = "Elizabeth"


def greeter():
    person = "Justin"
    print("Hi " + person + "!")


greeter()
print("Hi " + person + "!")
# Exercise: Variables in Functions
# Write a function in which you input the Celsius temperate and it outputs the Fahrenheit equivalent
print()
print("Exercise: Celsius to Fahrenheit")


def cels_to_fahr(cels_temp):
    fahr_temp = (1.8 * cels_temp) + 32
    return fahr_temp


print(cels_to_fahr(0))
print(cels_to_fahr(100))