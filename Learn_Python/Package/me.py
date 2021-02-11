print(__name__)

if __name__ == '__main__':
    print("this is the main file")

from package import add_food, remove_food
from package import discount

list_to_buy = []

add_food('apple', list_to_buy) # pass by reference
add_food('grapes', list_to_buy)
add_food('watermelon', list_to_buy)
remove_food('watermelon', list_to_buy)

print(discount(list_to_buy))

