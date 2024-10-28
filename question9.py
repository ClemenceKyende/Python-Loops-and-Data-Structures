def has_pair_with_sum(nums, target):
    """
    Accepts a list of integers and a target sum.
    Returns True if two distinct numbers in the list add up to the target sum, otherwise False.
    Uses a set to store visited numbers and check if target - num exists in the set.
    """
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
sample_list = [10, 15, 3, 7]
target_sum = 17
print(has_pair_with_sum(sample_list, target_sum))  # Output: True
