def minSubArrayLen(target, nums):
    n = len(nums)
    min_length = float('inf')
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += nums[end]

        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1

    return min_length if min_length != float('inf') else 0


# Example Usage:
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))  # Output: 2
