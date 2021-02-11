# def function(x, y, z):
#     return x, y, z
#
#
# print(function(1, 2, 3))
#
#
fun = lambda x, y, z: (x+ y+ z)

print(fun(1, 2, 3))


#
# --------------- Map ----------------
# -----------maps takes a function and a iterable (eg: list) ---------------------------
print('Map')
l = list(range(10))
l2 = list(range(11,22))
print(l)

square = lambda x,y: x*y
print(list(map(square, l,l2)))

# --------------------------------------

# filter don't compute, it only filter 
# map dont filter but it computes.

# -------------- filter ------------------
print('filter')
check_even = lambda x: x%2 ==0
mynums= [1, 2, 3, 4, 5, 6]
print(list(filter(check_even, mynums))) # takes function and a list as argument of filter()

print('single line lambda-filter function')
print(list(filter(lambda x : x%2 ==0, [1,2,3 ,4, 5, 6, 7, 8])))

# ------------------------------------------


#------------ Reducers ------------
print('Reducers')
import functools as f
import operator as o
li=[3,4,6,4,6,7]
sum= f.reduce(o.add, li)
print('Reducers',sum)

# -------------------- Accumulator --------------------------
print('Accumulator')

import itertools as i
list1 = [3,7,4,7]
print(' The summation of list 1 is :')
print(list(i.accumulate(list1,lambda x,y:x+y))) # sum at every loop and print


# -----------------------------------------

# fizz buzz
l = list(range(50))
fizzbuzz = lambda x: 'fizzbuzz'\
    if(x % 3 == 0 and x%5 == 0) \
    else('fizz' if x % 3==0 \
             else ('buzz' if x % 5==0 else x))

# print(list(map(fizzbuzz,l)))


# IIEF

# square of list
# print(list(map((lambda x: x*x), l)))
# print(' ')
#
# square of 5
# print((lambda x: x*x)(5))


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))














