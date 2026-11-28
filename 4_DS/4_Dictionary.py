# 1. What is a Dictionary?
# A dictionary stores data in key-value pairs.

# Think of it like a student's details:
# - Name → Rajan
# - Age → 21
# - Course → CSE

student = {
    "Name" : "Rajan",
    "Age": 21,
    "Course" : "CSE"
}
print(student)
print(student["Name"])

print()
# Adding and updating dictionary values
# In a dictionary, we can add a new key-value pair or update an existing value using the key.

# A. Adding a new item
student["College"] = "City"
print(student)
print(student["College"])

# B. Updating an existing item "College" --> "City"
student["Course"] = "Computer Science Engineering"
print(student)

# C. Updating Key in diction by removing exisitng Key
student["City"] = student.pop("College")            # it will upate the key College --> City the value will remain same
print(student)
print(student["City"])
print()
student["City"] = "Bangalore"                       # Value is updated for the City
print(student)
print(student["City"])

print()
# 1. len() — Count items
# len() counts how many key-value pairs are present in a dictionary.
print(len(student))

print()
# keys() — Get all keys
# keys() returns all the keys present in the dictionary.
print(student.keys())