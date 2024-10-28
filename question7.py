def remove_duplicates(lst):
    """
    Takes a list as input and returns a new list with duplicates removed.
    Iterates through the list and appends items to a new list if they are not already present.
    """
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Example usage:
sample_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(sample_list))
