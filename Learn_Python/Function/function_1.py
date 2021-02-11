list_to_buy = list()
# list should always be available

def add_food(food):
    if food not in list_to_buy:
        print('{} added to list'.format(food))
        list_to_buy.append(food)
    else:
        print('{} already added to list'.format(food))


def remove_food(food):
    if food in list_to_buy:
        print('{} remove from list'.format(food))
        list_to_buy.remove(food)
    else:
        print('{} not in list'.format(food))


food = add_food
list_to_buy = list()

food('apple')
food('watermelon')
# remove_food('apple')
print(list_to_buy)
