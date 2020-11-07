person = {
    'name': ' Rabin Phaiju',
    'age': 20,
    'gender': 'm',
    (1,2):12# keys in dict are tuple
}
print(person)

# inserting

# person['country'] = 'Nepal'
# person['hobbies'] = ['sports', 'reading']
# person['pet_names'] = {'cat': 'dog'}
# print(person)

# retreval

# print(person['name'])
# print(person.get('age', 'Not found'))

# deleting key value pair
# del person['age']
# print(person)

# .items() .keys() .values()
# print(person.items())
# print(person.keys())
# print(person.values())

# updating a existing key value pair
# person['country'] = 'Bhaktapur'
# print(person)

# for i in person.values():
#     print(i)

# for keys, values in person.items():
#     print(keys, values)


# merge two dictionary

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

d2.update(d1)
print(d2)














