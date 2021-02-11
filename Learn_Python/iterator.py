i = [1, 2, 3, 4, 5] # iterable
# next(i)
# print(dir(i))

# this is iterator
i_iterator = i.__iter__()
# print(dir(i_iterator))

# all iterable objects can produce an iterator object
# but they itself are not an iterator
print(next(i_iterator)) # 1
print(next(i_iterator)) # 2
print(i_iterator.__next__()) # 3
print(i_iterator.__next__()) # 4
print(i_iterator.__next__()) # 5
print(i_iterator.__next__())
