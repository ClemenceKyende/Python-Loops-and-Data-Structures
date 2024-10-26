def print_even_values_keys(d):
    """
    Prints keys from a dictionary where the corresponding values are even numbers.

    Args:
        d (dict): Dictionary with keys and integer values.
    """
    for key, value in d.items():
        if value % 2 == 0:
            print(key)


# Example usage
d = {'a': 2, 'b': 3, 'c': 4}
print("Keys with even values:")
print_even_values_keys(d)
