def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper  


@price_string
def new_price(quantity):
    return quantity * 0.9
