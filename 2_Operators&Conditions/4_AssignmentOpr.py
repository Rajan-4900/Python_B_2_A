# Assignment Operators
# Assignment operators are used to assign values to variables or update their existing values.

# Operator	    Example	        Same as
# =	            x = 10	        Assign 10
# +=	        x += 5	        x = x + 5
# -=	        x -= 5	        x = x - 5
# *=	        x *= 5	        x = x * 5
# /=	        x /= 5	        x = x / 5
# //=	        x //= 5	        x = x // 5
# %=	        x %= 5	        x = x % 5
# **=	        x **= 2	        x = x ** 2

# Example : 
x = 10
x += 5      # x = x+5 --> 10+5=15
print(f"Adding Value +5 = {x}")

x -= 5
print(f"Removing Value -5 = {x}")

a = 10
a *= 3
print(f"Multiplying: {a}")

b = 10
b /= 2
print(f"Deviding with 2 = {b}")

# Example question : 
c = 10
c += 5      # 10 + 5 = 15
c *= 2      # 15 * 2 = 30
c -= 10     # 30 - 10 = 20
c //= 2     # 20 // 2 = 10.0 -> 10   / final result -> 10

print(c)