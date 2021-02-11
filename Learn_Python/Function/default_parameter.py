price_of_food = {
    'apple': 100,
    'grapes': 300,
    'watermelon': 20
}
# print(price_of_food['apple'])

# shopkeeper started giving 50% discount


def discount(food, discount_rate=0.10):
    """
    this functions returns the discounted value
    """
    market_price = price_of_food[food]
    discount_amount = market_price * discount_rate
    price = market_price - discount_amount
    return price


print(discount.__doc__)
print(discount('apple', 0.5))
