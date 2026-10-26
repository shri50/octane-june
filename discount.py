def calculate_discount(price, discount_percentage=20):
    """
    Calculate the discounted price based on the original price and discount percentage.

    :param price: Original price of the item
    :param discount_percentage: Discount percentage to be applied (default is 20%)

    :return: Discounted price
    """
    discount_percentage = discount_percentage *0.01  # Convert percentage to decimal
    
    discounted_price = price * discount_percentage
    return price - discounted_price

print(calculate_discount(100))  # Output: 80.0
print(calculate_discount(100, 30))  # Output: 70.0
