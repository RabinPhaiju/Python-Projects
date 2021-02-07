# print(list(set([1,1,2,4,5,5,6,7])))

# list1 = ["ram","shyam",1,2,3,"hari"]
# list2 = ["shyam",2,3,10]

# print(list(set(list1) &  set(list2)))

# subset

# is
# a = [1,2]
# b = [3,4]
# print(a is b)

# Dictionary
# get function
# dict has unique key
x = [
    {"name":"ram","sem":6,"name": "rabin"},
    {"name":"shyam","sem":6},
    {"name":"hari","sem":6},
    {"name":"xyz","sem":6},
    {"name":"rabin","sem":6}
    ]

# print([i.get('name') for i in x])

# package is collection of module

import sys
print(sys.path)
# path of the module to search first

# do any searching algorithm