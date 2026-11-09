# Your practice assignment 💻

# Exercise 1 – Number Printing
# Print numbers from 1 to 20 using a for loop.
print("NUmber from 1 to 20:")
for i in range(1, 21):
    print(i)

print()
# Exercise 2 – Reverse Counting
# Print numbers from 10 to 1 using a for loop.
print("Reverse Counting: ")
for reverse in range(10, 0, -1):
    print(reverse)

print()
# Exercise 3 – Odd Numbers
# Print all odd numbers from 1 to 50 using a for loop.
print("Getting Only Odd Numbers: ")
for oddNum in range(1, 51, 2):
    print(oddNum)

print()
# Exercise 4 – Multiplication Table
# Take a number from the user and print its multiplication table from 1 to 10.
print("Mutiplcation Table: ")
user = int(input("Enter Multiplication Table Number: "))
print(f"Multiplcation Table For : {user}")
for multi in range(1, 11):
    print(f"{user} x {multi} = {user * multi}")

print()
# Exercise 5 – Sum of Numbers
# Take a number from the user and calculate the sum of all numbers from 1 to that number.
print("Calculating SUm Value for each Number: ")
sum =  int(input("Enter a Number: "))
total = 0
for cal in range(1, sum + 1) :
    total += cal
    print(total)
    