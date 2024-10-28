def keys_greater_than(dictionary, n):
    """
    Takes a dictionary and an integer n as input.
    Returns a list of keys where the corresponding value is greater than n.
    Uses list comprehension to filter keys based on their values.
    """
    result = [key for key, value in dictionary.items() if value > n]  # Check each key-value pair
    return result

# Example usage:
sample_dict = {'a': 5, 'b': 12, 'c': 3}
n = 4
print(keys_greater_than(sample_dict, n))  # Output: ['a', 'b']
