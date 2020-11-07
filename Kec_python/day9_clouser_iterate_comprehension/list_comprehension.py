# [expression for item in iterable ]
# [expression for item in iterable if condition ]


names = ['rabin', 'sabin', 'ram', 'hari', 'sopnam']

# print([i for i in names if i.startswith('r')])

list_even = []
list_odd = []
[list_even.append(i) if i % 2 == 0 else list_odd.append(i) for i in range(10)]
print(list_even, list_odd)


# nested loop ------------------------------------
mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 100]]
print(mylist)