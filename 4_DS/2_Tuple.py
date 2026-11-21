# Python Tuples
# A tuple is similar to a list, but the main difference is that we cannot change its elements after creating it.
# tuples are immutable, which means we cannot change their elements after creating them.

fruits = ("Apple", "Banana", "Mango", "Orange","Mango")
#fruits[1] = "Orange"            # TypeError: 'tuple' object does not support item assignment
#print(fruits)

print()
# Tuple Indexing
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
# print(fruits[4])        # IndexError: tuple index out of range

print()
# len() and count() in Tuples
# These methods work just like they do with lists.
print(len(fruits))      # length of the fruits tuple
print(fruits.count("Mango"))        # it will counts how many times the same element appears

print()
# index() method in Tuples
# The index() method returns the position of an element.
print(fruits.index("Orange"))

# Tuple with one element
a = (10, 20, 30)  # Tuple
b = (10)          # Integer, NOT a tuple
c = (10,)         # Tuple
# To create a tuple with only one element, we must add a comma ,.

print()
# Tuple Packing and Unpacking

# 1. Tuple Packing
# Putting multiple values into one tuple.
student = ("Rajan", 22, "CSE")
print(student)

# 2. Tuple Unpacking
# Assigning tuple elements to separate variables.
student = ("Rajan", 22, "CSE")
name, age, course = student
print(name)
print(age)
print(course)

print()
# What happens if variables don't match?
students = ("Rahul", 21, "Python")
names, ages = students
print(names)
# Python will raise a ValueError because the number of variables and values doesn't match.

