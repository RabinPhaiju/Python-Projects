# 1.If we list all the natural numbers below 10 that are multiple of
# 3 or 5 we get 3, 5, 6, 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# sum = 0
# for i in range(1000):
#     if i % 3 == 0:
#         sum += i
#     elif i % 5 == 0:
#         sum += i
#
# print(sum)


# The sum of the square of the first ten natural number is
# 12 + 22 + .... 102 = 385
# The square of the sum of the first ten natural number is,
# (1+2+3+....10)2 = 552 = 3025
# The difference between them is
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of
# the first one hundred natural numbers
# and the square of the sum

# summation = 0
# square = 0
# for i in range(100):
#     summation += i**2
#     square += i
# squares = square**2
# print(squares-summation)
#
# sum_of_sq = 0
# summ = 0
# for i in range(1,100,1):
#     sum_of_sq += i**2
#     summ += i
# sq_of_sum = summ**2
# diff = sq_of_sum - sum_of_sq
# print(diff)




# 2^15 = 32768 and the sum of its digit is 3 + 2 + 7 + 6 + 8 = 26
# what is the sum of the digits of the number 21000


number = 2**15
string = str(number)
sum = 0
for i in string:
    sum += int(i)
print(sum)

number = 2**1000
string = str(number)
sum = 0
for i in string:
    sum += int(i)
print(sum)
# >>1366







