# This file contains basic python operators

# Addition
print("Addition:", 6+10)

# Subraction
print("Subraction:", 5-7)

# Multiplication
print("Multplication:", 5*10)

# Division
print("Division:", 9/2)

# Floor Division
print("Floor Division:", 9//2)

# Modulo Division
print("Modulo Division:", 5%2)

# Exponent
print("Exponent:", 2**16)

x = 20
y = 7

# result = x + y
# print('Addition result', result)
#
# result = x - y
# print('Subtraction result', result)
#
# result = x / y
# print('Division result', result)
# result = x // y
# print('Floor result', result)

# result = x**y
# print('Exponent result', result)

age = 15

is_eligible = True if age > 18 else (True if age > 12 else False)
print(is_eligible)


# Comparision
print("Equality:", 1==1)
print("Inequality:", 1!=1)
print("Greater Than:", 2>1)
print("Greater Than Equals To:", 5>=5)
print("Less Than:", 1<2)
print("Less Than Equals To:", 5<=10)


# ------------------------------------------------
mylist = [10, 20, 30, 40, 50]

if 10 in mylist:
    print('Yes')

print(max(mylist))
print(min(mylist))
