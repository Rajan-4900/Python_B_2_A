# Exercise 1: Personal Information
# Create a Python program that asks the user for:
# 1. Name
# 2. Age
# 3. College name
# 4. Course
# Display all the information.

std_name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
college_name = input("Enter Your College Name: ")
course = input("Enter your Course Name: ")

print("Name: ", std_name)
print("Age: ", age)
print("College: ", college_name)
print("Course: ", course)

# Exercise 2: Simple Calculator
# Create a program that takes two numbers from the user and displays:
# - Addition
# - Subtraction
# - Multiplication
# - Division

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Division: ", num1/num2)

# Exercise 3: Age Calculator
# Create a program that asks for the user's birth year and calculates their approximate age.

birth_year = int(input("Enter Your Birth Year: "))
current_year = int(input("Enter Precent Year: "))
age = current_year - birth_year
print("Your Age Is: ", age)