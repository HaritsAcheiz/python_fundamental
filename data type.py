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
# arrays, arrays are a compact way of collecting basic data with similar data types,

# list,
# tuples,
# dictionary,
# sets,
# files