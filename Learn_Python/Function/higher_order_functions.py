# Functions returns and takes functions

# ----------------- Map ---------------------------
test_list = list(range(10))


def functions(x):
    return x * x


sq = tuple(map(functions, test_list)) # map returns a map , so we can save it in list or tuple
sq = list(map(functions, test_list)) # map returns a map , so we can save it in list or tuple
# print(type(sq))
# print(sq)
# -------------- OR --------------


def my_map(f, li):
    new_list = []
    for i in li:
        new_list.append(f(i))
    return new_list


square = my_map(functions, test_list)
# print(type(square))
# print(square)


# ----------Filter------- IS even ------------


def is_even(x):
    if x % 2 == 0:
        return True
    return False


# print(list(filter(is_even, test_list)))

# filter and map are same but
# map returns list with actual return value
# filter remove is the return is false from the list


# lambda
# print(list(filter(lambda x: is_even(x), test_list)))

# --------custom filter---------------
def my_filter(f, li):
    new_list = list()

    for i in li:
        if f(i):
            new_list.append(i)
    return new_list


# print(my_filter(is_even, test_list))


# -------------- return function ---------------- ODD EVEN


def odd_even(n):
    def odd():
        return 'this is odd'

    def even():
        return 'this is even'

    if n % 2 == 0:
        return even
    return odd


fun = odd_even(3)
# returns function saved in fun

print(fun())


# ---------------- zip -----------------------
list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = [100, 200, 300]


print(list(zip(list1, list2, list3)))

# ------------------ reduce -------------------
# next time the acc is the return value from last function call
from functools import reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, list1, 0))