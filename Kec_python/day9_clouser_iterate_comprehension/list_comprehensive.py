# person_name = 'rabin'
# letter = list(person_name)
# print(letter)

#
# letter = [i for i in person_name]
# print(letter)

# using lambda
# letter = list(map(lambda x: x, person_name))
# print(letter)

# even using for loop
# even = []
# for i in range(10):
#     if i % 2 ==0:
#         even.append(i)
# print(even)

# list comprehension
# even = [i for i in range(10) if i % 2 ==0]
# print(even)


# even for number greater than 5
# list comprehension with multiple with
# even = [i for i in range(10) if i % 2 == 0 if i > 5]
# even = [i for i in range(10) if i % 2 == 0 and i > 5]
# print(even)

# list comprehension with if else
# numbers = list(range(1, 11))
# check = []
# for i in numbers:
#     if i % 2 == 0:
#         check.append('even')
#     else:
#         check.append('odd')
# print(check)

# check = ['even' if i % 2 == 0 else 'odd' for i in numbers]
# check = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
# print(check)


# [[1, 2], [1, 2], [1, 2], [1, 2]]
test = []

for i in range(4):
    temp = []
    for j in range(1, 3):
        temp.append(j)
    test.append(temp)
print(test)
#
test = [[j for j in range(1, 3)] for i in range(4)]
print(test)
test = [list(range(1, 3)) for i in range(4)]
print(test)










