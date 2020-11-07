basket = {'orange', 'apple', 'grapes'}
shelf = {'apple', 'pear'}

# --------- delete from set --------------
# shelf.discard('apple')
# print(shelf)

# intersection
# print(basket.intersection(shelf))
# print(basket & shelf)

# union
# print(basket.union(shelf))
# print(basket | shelf)


# A - B
# print(basket.difference(shelf))
# print(basket - shelf)

# not(AnB)
# print(basket.symmetric_difference(shelf))
# print(basket ^ shelf)

# super set and sub set
basket = {'apple'}
shelf = {'apple', 'grapes', 'orange'}

# print(basket.issubset(shelf))
# print(shelf.issubset(basket))

# print(basket.issuperset(shelf))
# print(shelf.issuperset(basket))