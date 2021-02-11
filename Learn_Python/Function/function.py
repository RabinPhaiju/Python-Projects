# every function returns something, if nothing is return then '''None''' is returned

def adder(n1, n2):
    return n1 + n2

# print(adder(12, 23))

# keyword argument ------------------
def adder(n1, n2, n3):
    print(f'n1={n1}, n2={n2}, n3={n3}')
    return n1 + n2 + n3

# print(adder(n2=2, n1=4, n3=6))
# print(adder(1, n3=3, n2=2))


# recursion
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

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


# function overloading -> no function overloading in python




