def majorityElement(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [3, 2, 3]
print(majorityElement(nums))  # Expected Output: 3
nums = [2, 2, 2, 2]
print(majorityElement(nums))  # Expected Output: 2
nums = [-1, -1, -1, 2, 2, -1, 2]
print(majorityElement(nums))  # Expected Output: -1
