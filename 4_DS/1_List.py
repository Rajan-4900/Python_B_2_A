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

