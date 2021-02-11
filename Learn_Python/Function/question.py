# 1. Write a function to generate following pattern that takes number of rows as parameter (default to 5)
# *
# **
# ***
# ****
# *****

def pattern(n):
    for i in range(n):
        print('*' * (i + 1))


pattern(10)

# 2. Write a function to covert following list of tuples into dictionary.
price = [('orange', 100), ('watermelon', 200), ('papaya', 300)]


def dictionary(l):
    return dict(l)


print(dictionary(price))


# 3. Replace prime numbers with 'prime' string in a given list of integers
# using lambda function. (you can use separate function to check for prime)

def is_prime(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


test_list_1 = list(range(20))
test_list_1 = list(map(lambda x: 'prime' if is_prime(x) else x, test_list_1))
print(test_list_1)

# 4. write a function that takes list of numbers as input and returns a new
# list removing all prime numbers. (try using the same prime function)

test_list_2 = list(range(20))


def remove_prime(l):
    a = []

    for i in l:
        if not is_prime(i):
            a.append(i)

    return a


print(remove_prime(test_list_2))

# can also be done using filter function
print(list(filter(lambda x: not is_prime(x), test_list_2)))

# 5. A function takes two lists as arguments
# say, list_1 = [1,2,3,4] and list_2 = [1, 1] where, len(list_1) > len(list_2).
# Slide list_2 over list_1 from left to right (one step at a time) till the end.
#  Calculate the sum of the sum of the overlapped numbers of list_1 and list_2.
# list_1 and list_2 can be of any length and can contain any numbers.

list_1 = [1, 2, 3, 4]
list_2 = [1, 1]

sum = 0

for x in range(len(list_1) - len(list_2) + 1):
    for y in range(len(list_2)):
        sum += list_1[x + y] + list_2[y]

print('sum = ', sum)