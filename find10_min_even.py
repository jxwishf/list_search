def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    a = None

    for b in data:
        if b % 2 == 0:
            if a is None or b < a:
                a = b
    return a

