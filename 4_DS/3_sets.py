# Sets in Python
# A Set is a collection of unique elements. It automatically removes duplicate values.
numbers = {10, 15, 20, 21, 65, 10, 15, 80, 32}
print(numbers)
print(type(numbers))
print(len(numbers))

print()
fruits = {"Apple", "Banana", "Apple", "Mango", "Banana"}
print(len(fruits))
# output : Apple, Banana, Mango 

print()
# Adding elements to a Set — add()
# We use add() to insert a new element into a set.
fruits.add("Orange")
print(fruits)
print(len(fruits))

print()
# remove() method in Sets
# We use remove() to delete an element from a set.
numbers.remove(10)
print(numbers)
print(len(numbers))

print()
# discard() method
# discard() also removes an element from a set.
# remove() --->	Raises KeyError (Gives an error if the element doesn't exist.)
# discard() ---> No error (Does not give an error if the element doesn't exist.)
numbers.discard(85)
print(numbers)
print(len(numbers))

print()
# pop() in python
# In Python Sets, pop() removes an arbitrary element.
number = {10, 20, 30, 40}
removed = number.pop()
print("Removed:", removed)
print("Remaining:", number)


# Method	    What it does
# add()	        Adds an element
# remove()	    Removes a specific element
# discard()	    Removes an element without error if absent
# pop()	        Removes an arbitrary element
# clear()	    Removes all elements

print()

# Set operations — union()
# Union combines two sets and returns all unique elements.
a = {10, 20, 30}
b = {30, 40, 50}
result = a.union(b)
print(result)