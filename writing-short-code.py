# Define a function named convert that takes a list of numbers as its only parameter
# and returns a list of each number converted to a string.
# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
# What makes this tricky is that your function body must only contain a single line of code.

# time 1 min
def convert(nums):
    return [str(char) for char in nums]


nums = [1, 2, 4, 5]
print(convert(nums))
      
