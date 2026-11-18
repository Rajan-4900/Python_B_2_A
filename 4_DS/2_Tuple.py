# Python Tuples
# A tuple is similar to a list, but the main difference is that we cannot change its elements after creating it.
# tuples are immutable, which means we cannot change their elements after creating them.

fruits = ("Apple", "Banana", "Mango", "Orange")
#fruits[1] = "Orange"            # TypeError: 'tuple' object does not support item assignment
#print(fruits)

print()
# Tuple Indexing
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
# print(fruits[4])        # IndexError: tuple index out of range
