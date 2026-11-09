# For Loop in Python
# A for loop is used to repeat a block of code for a specific range or to go through items in a collection.

# Understanding range()
# The range() function generates a sequence of numbers.
# There are three ways to use it.

# 1. range(stop) : Example 
for i in range(5):      # It starts from 0 and stops before 5.
    print(i)            # Output : 0,1,2,3,4

print()
# 2. range(start, stop) : Example 
for a in range(1, 6):   # It starts from 1 and stops before 6.
    print(a)            # output : 1,2,3,4,5

print()
# 3. range(start, stop, step) : Example 
for b in range(2, 11, 2):   # It start from 2 adn ends befor 11-->10 and it will jump in 2 steps 
    print(b)                # Output : 2,4,6,8,10
