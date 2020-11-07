print(__name__)

if __name__ == '__main__':
    print("this is the main file")


# create a list of fruits to buy
# go to market and see the discount prices

# import food
# import prices
# from food import add_food, remove_food
# from prices import discount
# -------- absolute -----------
from packages.list.food import add_food, remove_food
from packages.shop.prices import discount

# -------- relative ----------- best way -- not working
# from .packages.list.food import add_food, remove_food
# from .packages.shop.prices import discount

list_to_buy = []

add_food('apple', list_to_buy) # pass by reference
add_food('grapes', list_to_buy)
add_food('watermelon', list_to_buy)
remove_food('watermelon', list_to_buy)

print(discount(list_to_buy))

