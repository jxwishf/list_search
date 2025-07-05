def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    a = 0

    for num in data:
        if num % 2 == 0:
            if a is None or num > a:
                a = num
    return a
