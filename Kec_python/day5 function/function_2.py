def add_food(f, my_list, price):
    food = f
    print(id(food), id(price), id(my_list))
    price = 200

    print(id(food), id(price), id(my_list))
    if food not in my_list:
        my_list.append(food)
        print('{} added to list'.format(food))
    else:
        print('{} already in the list'.format(food))


list_to_buy = list()
price = 100
food = 'orange'

add_food(food, list_to_buy, price)  # pass by reference
# list act as object when pass to a function is pass by reference
# print(list_to_buy)
print(price)
# but price is passed as value
print(id(food), id(price), id(list_to_buy))

# integer, string are e-mutable so passed as value
# list  are mutable so passed as reference
