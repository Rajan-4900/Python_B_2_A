# Logical Operators
# There are three main logical operators in Python:
# 1. and
# 2. or
# 3. not
a = 10
b = 20

# AND Operator :-> if even ONE condition is False, the entire result becomes False.

print(a < b and b > 15)     # True
print(a > b and b > 15)     # Flase
print(a < b and b < 15)     # False

print()
# OR Operator :-> If at least ONE condition is True, the entire result becomes True.
print(a > b or b > 15)
print(a > b or b < 15)
print(a < b or b < 15)

print()
# NOT Operator :-> The not operator reverses the result.
# - True becomes False.
# - False becomes True.

c = True
d = False
print(not c)
print(not d)
print(not (c and d))

print()
# Example :
l = True
o = False
g = True

print(l and g)          # True
print(l or o)           # True
print(not (l and o))    # True
print((l and o) or g)   # True