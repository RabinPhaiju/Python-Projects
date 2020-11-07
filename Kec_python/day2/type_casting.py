eg_list = [1, 2, 3, 4, 1]
eg_tuple = tuple(eg_list)
# print(eg_tuple, type(eg_tuple))

eg_set = set(eg_list)
# print(eg_set)


# given two list of name

x = ['ram', 'shyam', 'hari', 'john']
y = ['hari', 'sita', 'rita']

# print(set(x) & set(y))

first_sem_names = ['ram', 'shyam', 'hari', 'john']
second_sem_names = ['hari', 'sita', 'rita']

print(set(first_sem_names) - set(second_sem_names))

