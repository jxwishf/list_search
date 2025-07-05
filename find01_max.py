def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    a = data[0]
    for b in data[0]:
        if b>a:
            a=b
    return a
    