# While Loop in Python
# A loop is used to repeat a block of code multiple times. and ...
# The loop stops when the condition becomes False.

# Example : Q1
# Print Hello 5 times with the loop

i = 1
while i <= 5:
    print("Hello")
    i +=1

print()
# Example : Q2
# Print numbers from 1 to 10
n = 1
while n <= 10:
    print(n)
    n += 1

print()
# Example : Q3
# Print even numbers from 1 to 10
ev = 1
while ev <= 10:
    if ev % 2 == 0:
        print(ev)

    ev += 1

print()
# Exmaple : Q4
# Countdown
count = 5
while count >= 1:
    print(count)
    count -= 1

# Example : Q5 
# Multiplication Table -->      5 x 1 = 5
tbl = int(input("Enter Your Multiplication Table: "))
count = 1
while count <= 10:
    print(f"{tbl} x {count} = {tbl*count}")
    count += 1