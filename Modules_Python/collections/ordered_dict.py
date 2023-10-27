from collections import OrderedDict

d = {} # unordered
d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = "E"

for elem in d:
    print(elem)
    