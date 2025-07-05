def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    a = data[0]
    for b in data[1]:
        if b<a:
            a=b
    return a