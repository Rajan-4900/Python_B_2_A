# Python Lists
# A list is used to store multiple values in a single variable.
# We use square brackets [] to create a list.
# Important : Python uses index numbers to access list elements.

# Example :
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
numbers = [12 , 1 , 23 , 34 , 44 , 76 , 987 , 4]
mixed = ["Python", 21, 5.0, True]

# Accesing The Fruits List by index Values
print(fruits[0])  # Apple
print(fruits[1])  # Banana
print(fruits[2])  # Mango
print(fruits[3])  # Orange
print(fruits[4])  # Grapes

print()
# Changing A List element
fruits[4] = "watermelon" 
print(f"Updated Fruits for Grapes[4] is : {fruits[4]}")
print(fruits)           # Printing All elements in the List

print()

# Finding the length of a list
# Important: len() counts elements, whereas indexing starts from zero.
print(f"Length of the List is : {len(fruits)}")

print()

# Adding elements using append() :
# We use append() to add a new element at the end of a list.
fruits.append("Ananas")             # Added the New element in the fruites at the last
print(fruits)

# append() → Adds an element at the end.
# len() → Counts the total elements.

print()
# insert() method :
# We use insert() when we want to add an element at a specific position in a list.
# Unlike append(), which adds an element at the end, insert() adds it at the position you specify.

# Example : 
# fruits = ["Apple", "Banana", "Mango"]
# Use insert() to add "Orange" at index 1.
# Then print the updated list.
fruit = ["Apple", "Banana", "Mango"]
fruit.insert(1, "Orange")               # inserting the new value in the list based on the requiremtn place 
print(fruit)

# append("Orange") → Adds at the end.
# insert(1, "Orange") → Adds at index 1.

