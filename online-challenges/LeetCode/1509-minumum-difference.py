def min_difference(nums):
    n = len(nums)
    if n <= 4:
        return 0

    nums.sort()
    scenarios = [
        nums[-1] - nums[3],
        nums[-2] - nums[2],
        nums[-3] - nums[1],
        nums[-4] - nums[0]
    ]

    return min(scenarios)

