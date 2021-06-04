print(__name__)

price_of_food = {
    'apple': 100,
    'grapes': 300,
    'watermelon': 20
}


def discount(my_list, discount_rate=0.10):
    """
    this functions returns the discounted value
    """
    selling_price = {}
    for food in my_list:
        market_price = price_of_food[food]
        discount_amount = market_price*discount_rate
        price = market_price - discount_amount
        selling_price[food] = price
    return selling_price