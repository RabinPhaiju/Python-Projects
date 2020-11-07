# every function returns something, if nothing is return then '''None''' is returned

# def adder(n1, n2):
#     return n1 + n2
#
#
# def multiplier(n1, n2):
#     return n1 * n2
#
#
# def divider(n1, n2):
#     return n1 / n2
#
#
# def difference(n1, n2):
#     return n1 - n2


# print(adder(12, 23))
# print(multiplier(2, 12))
# print(divider(23, 5))
# print(difference(2, 5))


# take 2 no from user and display its addition, multiplication using function

# x = int(input("Enter 1st number"))
# y = int(input('Enter 2nd number'))

# print(adder(x, y))
# print(multiplier(x, y))


# keyword argument ------------------

# def adder(n1, n2, n3):
#     print(f'n1={n1}, n2={n2}, n3={n3}')
#     return n1 + n2 + n3
#
#
# print(adder(n2=2, n1=4, n3=6))
# print(adder(1, n3=3, n2=2))


# recursion

# def factorial(n):
#     if n <= 1:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(5))


# wap to take a no, from user and print the sum of its digit using recursion
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum(n//10)
#
#
# x = int(input("enter a number"))
# print(sum_of_digits(x))

# a = 10
# b = a
# print(id(a))
# print(id(b))
# a = 11
# print(id(a))
# print(id(b))
# print(b)


# def something(arg, b):
#     arg.append(10)
#     arg.append(20)
#     b = 20 # search 1st in local and then global
#
#
# b = 10
# a = [1, 4, 5]
# something(a, b)
# print(a)
# print(b)


# global inside function
# total = 0
#
#
# def adder(arg1, arg2):
#     # global total
    # total = arg1 + arg2
    # print(f'total is {total}')
#
#
# adder(10, 20)
# print(total)


# default arguments
# def something(x, y, z=10):
#     print(f'x = {x}, y = {y}, z = {z}')
#
#
# something(y=10, x=20)


# function overloading --- no function overloading in python-----
# def adder(x, y):
#     print(x + y)
#
#
# def adder(x, y, z):
#     print(x + y + z)
#
#
# print(adder(2, 3))
# print(adder(2, 3, 4))





