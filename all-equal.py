# Define a function named all_equal that takes a list and checks whether all elements in the list are the same.
# # For example, calling all_equal([1, 1, 1]) should return True.
# time 12 min
def all_equal(nums):
    if not nums:
        return False
    elif min(nums) == max(nums):
        return True
    else:
        return False


# return all(digit == nums[0] for digit in nums)


nums = []
print(all_equal(nums))
