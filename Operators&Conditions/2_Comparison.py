# What are Comparison Operators?
# Comparison operators are used to compare two values.

# Python checks the condition and gives us one of two answers:
# - True – Condition is correct.
# - False – Condition is incorrect.

#  Comparison operators (==, !=, >, <, >=, <=)

# Example :
a = 10
b = 20

print(f"A is greater Than B: {a>b}")
print(f"A is Less Than B: {a<b}")
print(f"A is Equal To B: {a==b}")
print(f"A is Not Equal To B: {a!=b}")
print(f"A is Greate Or Equal To B: {a>=b}")
print(f"A is Less Than Equal To B: {a<=b}")

# Remember:
#  = means assigning a value.
#  == means comparing two values.

# Example : 
# Create a Python program that:
# 1. Takes two numbers from the user.
# 2. Checks whether both numbers are equal.
# 3. Checks whether the first number is greater.
# 4. Checks whether the first number is smaller.
# 5. Checks whether both numbers are different.

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print(f"Number are equal: {num1 == num2}")
print(f"First number is greater: {num1 > num2}")
print(f"First number is smaller: {num1 < num2}")
print(f"Number are different: {num1 != num2}")