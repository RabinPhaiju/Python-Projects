print(__name__)

def add_food(food, my_list):
    if food not in my_list:
        my_list.append(food)
        print('{} added to list'.format(food))
    else:
        print('{} already in the list'.format(food))
    return my_list


def remove_food(food, my_list):
    if food in my_list:
        my_list.remove(food)
        print('{} remove from list'.format(food))
    else:
        print('{} not in list'.format(food))
    return my_list

    