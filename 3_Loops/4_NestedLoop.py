# Nested loops in python
# A nested loop means a loop inside another loop.
# - Outer loop: Controls how many times the inner loop runs.
# - Inner loop: Completes all its iterations for every single iteration of the outer loop.

# Sample Code :
for i in range(1,4):
    for j in range(1,3):
        print(i,j)

# Important: The inner loop completes all its iterations before the outer loop moves to the next iteration.

print()
# Example 1:
# Star pattern ⭐
for a in range(1,4):
    for b in range(1,4):
        print(b, end=" ")
    print()

print()
# Example 2:
for a in range(1, 4):
    for b in range(1, 5):
        print(b, end=" ")
    print()
