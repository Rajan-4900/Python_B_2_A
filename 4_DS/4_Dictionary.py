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