from collections import defaultdict
# A default dict will bever raise a KeyError. Any key tat does not exist gets the value returned  by the default factory.


d = defaultdict(object)

print(d['one'])

d = defaultdict(lambda : 0)

print(d['one'])
d['two'] = 2
print(d['two'])