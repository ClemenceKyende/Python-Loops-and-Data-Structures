def has_pair_with_sum(nums, target):
    """
    Accepts a list of integers and a target sum.
    Returns True if two distinct numbers in the list add up to the target sum, otherwise False.
    Uses a set to store visited numbers and check if target - num exists in the set.
    """
    seen = set()  # Initialize an empty set to store visited numbers
    for num in nums:
        if target - num in seen:  # Check if the required number to reach the target exists in seen
            return True  # Pair found that adds up to target
        seen.add(num)  # Add the current number to seen for future checks
    return False  # Return False if no pair adds up to the target

# Example usage:
sample_list = [10, 15, 3, 7]
target_sum = 17
print(has_pair_with_sum(sample_list, target_sum))  # Output: True
