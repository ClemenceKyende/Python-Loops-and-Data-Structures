def tuples_to_dict(tuples):
    """
    Takes a list of tuples, each containing a string and an integer.
    Returns a dictionary where the strings are the keys and the integers are the values.
    Uses dictionary comprehension to construct the dictionary.
    """
    result = {key: value for key, value in tuples}  # Unpack each tuple to key-value pairs
    return result

# Example usage:
sample_tuples = [("apple", 5), ("banana", 3), ("cherry", 7)]
print(tuples_to_dict(sample_tuples))  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}
