def max_in_tuple(t):
    """
    Finds and returns the largest number in a tuple.

    Args:
        t (tuple): Tuple of numbers.

    Returns:
        int: The largest number in the tuple.
    """
    largest = t[0]
    for num in t:
        if num > largest:
            largest = num
    return largest


# Example usage
t = (10, 20, 30, 40, 50)
print("Largest number in tuple:", max_in_tuple(t))
