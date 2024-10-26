def reverse_strings(strings):
    """
    Reverses each string in a list and returns a new list of reversed strings.

    Args:
        strings (list): List of strings to reverse.

    Returns:
        list: New list with each string reversed.
    """
    reversed_list = [string[::-1] for string in strings]
    return reversed_list


# Example usage
strings = ["apple", "banana", "cherry"]
print("Reversed list:", reverse_strings(strings))
