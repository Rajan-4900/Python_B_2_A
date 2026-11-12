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