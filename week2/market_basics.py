"""Meeting 1 starter. No AI needed. Run: python week2/market_basics.py
Notebooks named below are in week1/notebooks/.
Stuck after trying? See solutions/week2/market_basics.py."""


def calculate_total(price, quantity):
    # TODO 1: Reject a quantity of zero or less.
    #   How: write an if statement. Inside it: raise ValueError('your message').
    #   raise stops the function and reports the problem. It is new here, not in the notebooks.
    #   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 3 (Decisions).
    # TODO 2: Return price * quantity, then delete the raise NotImplementedError line.
    #   Practice: week1-assignment.ipynb, Challenge 6 (a function that uses if and return).
    # Check: predict the answer first. calculate_total(8, 3) gives 24.
    # Then try quantity 0 and 'three'. Read the last line of each error.
    #   Help: week1-deepdive-1-python-speaks.ipynb, section 2 (reading errors).
    raise NotImplementedError('Complete calculate_total during Meeting 1.')


if __name__ == '__main__':
    try:
        print(calculate_total(8, 3))
    except NotImplementedError as exc:
        print(exc)
