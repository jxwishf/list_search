def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    a = None

    for b in data:
        if b % 2 != 0: 
            if a is None or b < a:
                a = b
    return a

