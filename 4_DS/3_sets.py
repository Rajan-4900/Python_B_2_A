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