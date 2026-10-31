"""Solution for Meeting 1. Try week2/market_basics.py yourself first.
Run: python solutions/week2/market_basics.py"""


def calculate_total(price, quantity):
    # TODO 1: stop early when the quantity makes no sense.
    if quantity <= 0:
        raise ValueError('Quantity must be greater than zero.')
    # TODO 2: this line only runs when the quantity is valid.
    return price * quantity


if __name__ == '__main__':
    print(calculate_total(8, 3))
