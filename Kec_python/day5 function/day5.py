# 1. Write a function to generate following pattern that
# takes number of rows as parameter (default to 5)
# *
# **
# ***
# ****
# *****


# def pattern(row=5):
#     row += 1
#     for i in range(row):
#         print('*' * i)
#
#
# pattern()


# 2. Write a function to covert following list of tuples into dictionary.
# price = [('orange', 100), ('watermelon', 200), ('papaya', 300)]

# def my_list(lists):
#     di = dict()
#     for i, j in lists:
#         di[i] = j
#     return di
#
#
# price = [('orange', 100), ('watermelon', 200), ('papaya', 300)]
# print(my_list(price))


# 3. Replace prime numbers with 'prime' string in a given
# list of integers using lambda function. (you can use separate function to check for prime)

# prime = list()
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime.append(i)
#
#
# l = list(range(100))
# print(list(map((lambda x: 'prime' if x in prime else x), l)))


# 4. Write a function that takes list of numbers as input and
# returns a new list removing all prime numbers. (try using the same prime function)

# prime = list()
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime.append(i)
#
#
# def prime_remove(l):
#     li = list()
#     for i in l:
#         if i not in prime:
#             li.append(i)
#     return li
#
#
# lists = list(range(100))
# print(prime_remove(lists))


# 5. A function takes two lists as arguments say,
# list_1 = [1,2,3,4] and list_2 = [1, 1] where, len(list_1) > len(list_2).
# Slide list_2 over list_1 from left to right (one step at a time) till the end.
# Calculate the sum of the sum of the overlapped numbers of list_1 and list_2.
# list_1 and list_2 can be of any length and can contain any numbers.


# def sum_list(list1, list2):
#     sum2 = 0
#     le1 = len(list1)
#     le2 = len(list2)
#     diff = le1-le2
#     for i in range(diff+1):
#         sum1 = 0
#         for j in range(le2):
#             sum1 += list1[i+j]+list2[j]
#         print(sum1)
#         sum2 += sum1
#     return sum2
#
#
# list_1 = [1, 2, 3, 4]
# list_2 = [1, 1]
# print(sum_list(list_1, list_2))

