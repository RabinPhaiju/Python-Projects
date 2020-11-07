# 1. Write a Python program that takes two lists and prints True if they have at least one common member.
seta = ['ram', 'shyam', 'hari', 'krishna']
setb = ['krishna', 'subadra', 'kishor', 'ram']
# print(any(item in setb for item in seta))


# 2. Write a Python program to remove duplicates from a list.
# using set
a = [1,2,3,4,1,2,3]
b = set(a)
# print(b)
# or ----- using dictionary ------------
b = list(dict.fromkeys(a))
# print(b)


# 3. Write a program to generate a list that contains the squares of first 100 prime numbers.
# prime_sqr = list()
# for i in range(100):
#     if i==2 or i==3 or i==5 or i==7:
#         prime_sqr.append(i**2)
#     elif i%2==0 or i%3==0 or i%5==0  or i%7==0 or i==1:
#         pass
#     else:
#         prime_sqr.append(i**2)
# print(prime_sqr)

# --------------- or optimized --------------
# prime = list()
# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         prime.append(i**2)
#
# print(prime)


# 4. Write a program to print out the frequencies of letters in a USER INPUT string.
# string = 'This is a test'
# string = string.lower()
# count = dict()
# for i in string:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# print(count)


# 5. Write a program to merge two dictionaries into one.

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
print(any(item in d1 for item in d2))

d1.update(d2)
print(d1)










