# Break in loop
# break immediately stops the entire loop.

# Example :
for i in range(1, 6):
    if i == 4:
        break               # it will checks the iterations till 4 if 4 appears then it stop the loop 
    print(i)

# How does it work :
# i = 1 ---> print 1
# i = 2 ---> print 2
# i = 3 ---> print 3
# i = 4 ---> condtion become True 
# break stop the loop and it will not print 4

print()
# Continue in loop
# continue skips the current iteration and moves to the next iteration.
for a in range(1, 6):
    if a == 4:
        continue            # it is skiped 4 and continued to next iteration

    print(a)

# how does it works:
# i = 1 --> print 1
# i = 2 --> print 2
# i = 3 --> print 3
# i = 4 --> skips this iteration it will nt print this value
# i = 5 --> print 5
# i = 6 --> print 6

print()
# Example Question :
# Write a Python program using a for loop.
# Requirements:
# 1. Print numbers from 1 to 10.
# 2. Skip number 5 using continue.
# 3. Stop the loop when the number reaches 8 using break.

for b in range(1, 11):
    if b == 5:
        continue
    if b == 8:
        break
    print(b)
