# dictionary
## a dictionary is a type of collection which consists of key value pair.
## the keys and values can be of any type.
## a dictionary is indexed through the keys.
## same key cannot be assigned.


fruits = ['orange', 'watermelon', 'grapes', 'mango']
price = [100, 200, 300, 400]

# empty dict
price_of_fruits = {}
print(price_of_fruits, type(price_of_fruits))

price_of_fruits = dict()
print(price_of_fruits, type(price_of_fruits))

# dict = key:value
price_of_fruits = {
    'orange': 50,
    'watermelon': 200,
    'grapes': 300,
    'mango': 400
}
print(price_of_fruits)

print(price_of_fruits['orange'])

min_max = {
    'orange': [50, 200],
    'watermelon': [20, 300],
    'grapes': [300, 400],
    'mango': [400, 500]
}
keys = min_max.keys()
values = min_max.values()
print(keys, values)
print(min(min_max.values()))

min_max['apple'] = 900 # add key-values

print(min_max)
