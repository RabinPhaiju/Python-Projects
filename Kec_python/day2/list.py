# build in data types

# empty list
fruits = list()
print(fruits, type(fruits))

# list
# define list if fruits -. can have any datatype
fruits = ['apple', 'banana', 'carrot', 'apple', 12]
country=['nepal','nepali']
print(fruits + country)


print(len(fruits))
print(fruits + fruits)
print(fruits[2:])
new_fruits = fruits.copy()
new_fruits[1] = 'rabin'
print(new_fruits)
new_fruits.pop()
new_fruits.pop(2) # here the argument refers to the positional value
print(new_fruits)



# print(fruits[0])

# slicing
summer_fruits = fruits[:2]
# print(summer_fruits)

winter_fruits = fruits[2:]
# print(winter_fruits)

# edit list
fruits[0] = 'Apples'
# print(fruits)
# print(fruits[-1])
# print(fruits[-2])
# print(fruits[0:-1:2])

# length
# print(len(fruits))

# delete
print(fruits)
del fruits[0]
print(fruits)

# remove
fruits.remove('apple')  # only the first matching entry is removed from left side

# insert -> Append adds an element to the end of the list
# append cannot add two value at once
fruits.insert(2, 'syau') # syau will be inserted into the second position of the list
fruits.append(1)
fruits[0] = 'apples'
print(fruits)

# extend
li= [1,2,3]
li.extend([4,5,6])
print(li)


# check for an existence of an element in the list
print(3 in li) # the 'in' statement checks whether an element is present in the list.

# Max and Min
print(max(li))
print(min(li))

# -------------------------- 2D list --------------------------


# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# # print(matrix[0][2])
#
# for row in matrix:
#     for item in row:
# 


# sort list ----------------------
sort1 = ['a', 'z', 'g', 'k', 'h']
sort2 = [1, 4, 6, 54, 3]
sort1.sort() # modify the orignal list
print(sort1)
print(sorted(sort1)) # wont change the original list