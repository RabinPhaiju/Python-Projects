days = ['Sunday', 'Monday', 'Tuesday']

# append()
# days.append('Wednusday')
# print(days)

# extend() to append multiple
# days.extend(['Friday', 'Saturday'])
# print(days)

# insert in the middle
# days.insert(1, 'morining')
# print(days)

# insert multiple in the middle
# days = days[:2] + ['random day 2','random day 3'] + days[2:]
# print(days)

# remove()
# days.remove('random day 2')
# print(days)

# pop()
# days.pop(1)
# print(days)

# sort
# some_arr = [10, 34, 45, 56, 45]
# some_arr.sort()
# print(some_arr)

# reversal
# print(days[::-1]) # without affecting values
# days.reverse()
# print(days)


# list and tuple unpacking-----------------
# sun, mon, tue = days
# print(sun, mon, tue)
#
# days = tuple(days)
# sun, mon, tue = days
# print(sun, mon, tue)

# print('sunday' in days) # returns true or false


#check the list contains elements of another list ------all----------
# List1 = ['python', 'javascript', 'csharp', 'go', 'c', 'c++']
# List2 = ['csharp', 'go', 'python']
# check = all(item in List1 for item in List2)
# print(check)

# check the list contains elements of another list ----any------
# List1 = ['python', 'javascript', 'csharp', 'go', 'c', 'c++']
# List2 = ['swift', 'php', 'python']
# check = any(item in List1 for item in List2)
# print(check)

# list unpacking -----------------------
a,b,c,*other = [1, 2, 3, 4, 5, 7, 8]
print(a)
print(b)
print(c)
print(other)


# ----------- clear -------------------
some_arr = [10, 34, 45, 56, 45]
some_arr.clear()
print(some_arr)












