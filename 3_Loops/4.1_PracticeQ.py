# Practice 1: Print stars using nested loops
# what is the code for this output :
# * * *
# * * *
# * * *
for i in range(1,4):
    for i in range(1,4):
        print("*", end=" ")
    print()

print()

# Now try to print this pattern:
# * * * *
# * * * *
# * * * *
for a in range(1, 4):       # 3 rows
    for b in range(1, 5):   # 4 stars in each row
        print("*", end=" ")
    print()                 # Move to next row

print()

# example : : Increasing star pattern ⭐
# output :
# *
# * *
# * * *
# * * * *
for c in range(1,5):
    for d in range(1, c+ 1):
        print("*", end=" ")
    print()

print()
# Decreasing star pattern ⭐
# * * * *
# * * *
# * *
# *
for e in range(1, 5):
    for f in range(1, 6 - e):
        print("*", end=" ")
    print()