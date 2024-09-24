def threeSum(nums):
    """
    This function finds all unique triplets in the given list of integers that sum up to zero.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    List[List[int]]: A list of lists, where each inner list represents a unique triplet that sums up to zero.
    """
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result
