# list
# eg_list = [1, 2, 3]
# print(eg_list, type(eg_list))
# print(eg_list[-1])

# list inside list
# eg_list1 = ['ram', 2, ['patan', 'ktm', 'lalitpur'], 5,34]
# print(eg_list1[2])
#
# eg_list2 = [1, 2, 3, [200, 300, [100, [400, [18, [19]]]]]]
# print(eg_list2[3][-1][1][1][1][0])

# eg_list = [1, 2, 3]
# eg_list1 = [4, 5, 6]
# print(eg_list)
# eg_list.append(4)
# print(eg_list)
# new_list = eg_list + eg_list1
# print(new_list)
# new_list.pop(0)
# new_list.pop()
# print(new_list)


# ------ tuple -------------- new value cannot be added/removed
# eg_tuple = (0, 1, 2, 3)
# eg_tuple1 = 3, 4, 5, 6
# eg_tuple2 = 4,
# eg_tuple3 = (4) # int
# print(eg_tuple, print(eg_tuple1), print(eg_tuple2))
# print(eg_tuple3, type(eg_tuple3))

# eg_tuple = ('Ram', 21, 'Engineering College', 67.98)
# print(eg_tuple[-1])

# eg_list = [1, 2, 3]
# eg_tuple = (1, 2, 3)
# print(1 in eg_tuple)
# print(2 in eg_list)


# dictionary---------no index----use key---- order maintain hudaina

eg_dict = {
    'name': 'rabin',
    'roll': 23,
    'college': 'Khec',
    '1': '1.1'
}
eg_dict1 = dict(
    name='rabin',
    roll=23,
    college='khec'
)

# print(eg_dict['name'])
# print(eg_dict)
# print('your name is {}. your roll is {}. your college is {}'.format(eg_dict['name'],eg_dict['roll'],eg_dict['college']))

# print(dir(dict))

# update and insert
eg_dict['location'] = "Bhaktapur"
# print(eg_dict)

# if we access the key not available ->returns None or default value
# print(eg_dict.get('home','default'))

# check if key exist in dict
# print('name' in eg_dict)


# ---------------- SET ---------- unique key
# key cannot be diff type
# no duplicate
# represented as {}
# don't maintain order - no indexing
# mutable

eg_set = {'name', 2, 'age', 'last'}
# print(eg_set)
# print(dir(set))

eg_set.add('hello')
# print(eg_set)

eg_set1 = {'name', 2, 'age', 'help'}
print(eg_set | eg_set1) # union
print(eg_set & eg_set1) # intersection
print(eg_set1 - eg_set) # difference
print(eg_set - eg_set1)


# sub-set




