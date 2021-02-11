# generator
# yield
# generator func always returns an iterator


# def square(num):
#     return num**2
#     yield num**2


# test = square(2)
# print(next(test))


# def my_gen(a):
#     return a
#     a += 1
#
#
# print(my_gen(0))
# print(my_gen(0))


# def my_gens():
#     a = 0
#     print('First')
#     yield a
#
#     a += 1
#     print('Second')
#     yield a
#
#     a += 1
#     print('final')
#     yield a
#
#
# temp = my_gens()
# print(next(temp))
# print(next(temp))
# print(next(temp))
# print(next(temp)) # stopinteration

# my gen function returns iterator()
# for i in temp:
#     print(i)
# my_gen() is iterable,
# temp is value


# while in generator
# def test():
#     a = 0
#     while True:
#         yield a
#         a += 1
#      # print(a)
#
#
# a_test = test()
# print(next(a_test))
# print(next(a_test))
# print(next(a_test))
# print(next(a_test))

# for i in a_test(): # the for loop never ends

