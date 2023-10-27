t = (1, 2, 3)
# print(t[0])

from collections import namedtuple
# named tuple is a quick way to create class

Dog = namedtuple('Dog','age bread name')
sam = Dog(age=2, bread='lab', name='sammy')
print(sam.age)

Cat = namedtuple('Cat', 'fur claws name')
c = Cat('Fuzzy', False, 'kitty')

print(c.fur)