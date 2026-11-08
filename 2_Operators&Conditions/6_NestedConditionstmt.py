# Nested if statements
# A Nested if means writing one if statement inside another if statement.

# 1. Login System
# Imagine a website login system:
# 1. First, check whether the user has entered the correct username.
# 2. If the username is correct, check the password.
# 3. If both are correct, allow login.

user_name = input("Enter Username: ")

if user_name == "admin":

    user_password = input("Enter user password: ") 
    if user_password == "12345":
        print("Login Succesfull!")
    else:
        print("Password is incorrect")

else:
    print("User name is incorrect")

# 2. Exam Eligibility
# Suppose a student must:
# - Have at least 75% attendance.
# - Score at least 35 marks.

attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:

    marks = int(input("Enter your marks: "))
    if marks >= 35:
        print("You are eligible to pass")
    else:
        print("You are not eligible to pass")

else:
    print("You are not eligible to take exam")

# 3. Driving Eligibility
# - Takes the user's age.
# - If age is 18 or above, ask whether they have a driving licence.
# - If licence is yes, print You can drive.
# - Otherwise print You need a driving licence.
# - If age is below 18, print You are not eligible to drive.

age = int(input("Enter Your Age: "))

if age >= 18:

    dl = input("Do you have a driving licence : ").lower()
    if dl == "yes":
        print("You can drive")
    else:
        print("You need a driving licence")

else:
    print("Your not eligible to drive")