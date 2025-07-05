def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    a = 0

    for b in data:
        if b % 2 != 0:
            if a is None or b > a:
                a = b
    return a