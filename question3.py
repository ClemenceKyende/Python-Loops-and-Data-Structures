def sum_of_list(nums):
    """
    Calculates and returns the sum of all numbers in a list.

    Args:
        nums (list): List of numbers to sum up.

    Returns:
        int: Sum of all numbers in the list.
    """
    total = 0
    for num in nums:
        total += num
    return total


# Example usage
nums = [1, 2, 3, 4, 5]
print("Sum of list:", sum_of_list(nums))
