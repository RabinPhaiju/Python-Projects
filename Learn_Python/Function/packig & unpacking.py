# *args returns tuple
# **kwargs returns dict

# packing


# def add_to_list(a, b, c):
#     print(a, b, c)
# add_to_list('apple', 'watermelon', 'pineapple')


# def add_to_list(*args):
#     if args is not None: # if args is empty
#         for i in args:
#             print(i)
# add_to_list('apple', 'watermelon', 'pineapple', 'syau')


# unpacking

# def add_to_food(*args):
#     if args is not None:
#         for i in args:
#             print(i)
# food = ['apple', 'papaya', 'orange', 'watermelon']
# add_to_food(*food)


# --------- dictionary -------------

def add_to_basket(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print(key, value)


# add_to_basket(apple=100, grapes=200, orange=20)

price_of_food = {
    'apple': 200,
    'grapes': 300,
    'watermelon': 20
}

add_to_basket(**price_of_food)












