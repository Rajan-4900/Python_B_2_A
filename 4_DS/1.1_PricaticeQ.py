# Practice question :
# Create a list containing these five names:
# Rajan, Rahul, Amit, Kiran, Rohit
# Then:
# 1. Print the complete list.
# 2. Print the first name.
# 3. Print the third name.
# 4. Change Rahul to Vijay.
# 5. Print the updated list.
# Hint: Remember that indexing starts from 0.

name = ["Rajan", "Rahul", "Amit", "Kiran", "Rohit"]
print(f"Printing the complete List : {name}")
print(f"Printing the first name : {name[0]}")
print(f"Printing The third name : {name[2]}")

# Chaning the element of Rahul to Vijay
name[1] = "Vijay"
print(f"Printing the Updated List : {name}")

print()
# Python Lists – Removing Elements
# Step 1: remove() method
names = ["Rajan", "Rahul", "Amit", "Kiran", "Rohit"]
# Your tasks:
# 1. Remove "Amit" using remove().
# 2. Print the updated list.
# 3. Print the length of the updated list.
names.remove("Amit")
print(f"Updated Names List : {names}")
print(f"Length of the List : {len(names)}")

print()
# Step 2: pop() method
std_names = ["Rajan", "Rahul", "Amit", "Kiran", "Rohit"]
# Your tasks:
# 1. Remove "Amit" using pop().
# 2. Print the updated list.
# 3. Print the length of the updated list.
std_names.pop(2)
print(f"Updated List : {std_names}")
print(f"The Length of Updated list : {len(std_names)}")