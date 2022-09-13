"""
This program created to learn data type in python
"""
#Data Type

# Data type is a set of possible values and a set of allowed operations on it
# Python use dynamic data types that are dynamic in nature and don't require initialization at the time of declaration
# Some programming language use static data typed that require explicit definition of a data type
# when they create a piece of data (e.g. variable, parameter, return value)
# Example:

# In Java
# int mynumber = 4 //integer data type, mynumber variable is only accept integer data
# string myname = 'Dudung' //string data type, myname variable is only accept string data
# float phi = 3.14 //float data type, phy variable is only accept float data

# In Python
mydata = 4 #variable become integer data type
print(type(mydata))
mydata = 'Dudung' #variable become string data type
print(type(mydata))
mydata = 3.14 #variable become float data type
print(type(mydata))


# Now we are focus on data type in python
# Data types in python can be defined into 2 group based on an application,
# Primitive data types and Non-Primitive data types

# Primitive data type
# Primitive data types are a set of basic data types from which all other data types are constructed.
# It's used almost in every programming languages.
# include:
# integer, An integer data type represents some range of mathematical integers.
mydata = 4 #variable become integer data type
print(type(mydata))
# float, A floating-point number represents a single precision rational number (6-7 significant digits) that may have a fractional part.
mydata = 3.14 #variable become float data type
print(type(mydata))
# boolean,  boolean is typically a logical type that can have either the value "true" or the value "false".
mydata = True #variable become float data type
print(type(mydata))
# char, It is a data type that holds one character (letter, number, etc.).
# But in python if you assign one character it would be considered as string data type
mydata = 'C'
print(type(mydata))

# Non Primitive data type
# non-primitive data is not a basic data types that only store values,
# but its constructed by collection of values with one or more basic data types.
# include:
# arrays, arrays are a compact way of collecting basic data (simply called sequence data types) with similar types (homogeneous).
# Arrays are sequence data types that behave very much like lists, except that the type of objects stored in them is constrained

import array as arr
int_array = arr.array("I",[1,2,3])
print(type(int_array))

# import array as arr
# int_array = arr.array("I",['a','b','c'])
# print(type(int_array))

# list, Lists are sequence data types that can store collection of heterogeneous or homogeneous items.
# Its written as a list of comma-separated element enclosed within square brackets.
# List are muteable, its mean that you can change their content without change their identity

l = [] #define empty list
print(type(l))

int_list = [1,2,3,4]
print(int_list)
print(type(int_list))

mixed_list = [1,'a',0.5]
print(mixed_list)
print(type(int_list))
mixed_list[0] = 5
print(mixed_list)

# tuples,
# Tuples are a immutable standard sequence data type that can store collection of heterogeneous or homogeneous items ,
# immutable means that once it's defined, you cannot delete, add or edit any values inside it.
# Its written as a list of comma-separated element enclosed within parentheses.

t = () #define empty tuples
print(type(t))

mixed_tuple = (1,'a',0.5)
print(mixed_tuple)
print(type(mixed_tuple))

# mixed_tuple[0] = 5
# print(mixed_tuple)

# dictionary,
# Dictionary are a mutable sequence data type that can store collection of heterogeneous or homogeneous items ,
# Dictionaries are written as a list of comma-separated key-value pairs enclosed within curly brackets.
# key is used to identify the item and the value holds the value of the item they are separated with colon ":".
# While keys and values are immutable and can be any type of data.

d = {} #define empty dictionary
print(type(d))

mixed_dict = {'a':1,'b':2,'c':0.5}
print(mixed_dict)
print(type(mixed_dict))

print(f"Value for item a is {mixed_dict['a']}")

mixed_dict['a'] = ['budi','naya','jamet']
print(mixed_dict)
print(f"Value for item a is {mixed_dict['a']}")
print(f"Value for item a is {mixed_dict['a'][0]}")


# sets,
# Sets are an unordered sequence data type of unique elements.
# They are mutable and written within curly brackets, but have no same value.

mixed_list = ['a','b','c','b','c','c']
mixed_set = set(mixed_list)
print(mixed_set)
print(type(mixed_set))