def calculate_discount(price):
    """
    Calculate the discounted price based on the original price and discount percentage.

    :param price: Original price of the item

    :return: Discounted price
    """
    
    discounted_price = price * 0.10
    return price - discounted_price

print(calculate_discount(100))  # Output: 90.0