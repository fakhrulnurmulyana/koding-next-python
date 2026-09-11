def calculate(price, discount, quantity):
    total = price * quantity
    discount_amount = total * discount / 100
    final_price = total - discount_amount

    return final_price
