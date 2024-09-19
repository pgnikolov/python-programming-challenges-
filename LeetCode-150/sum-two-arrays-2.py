def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        sum = numbers[left] + numbers[right]

        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left += 1
        else:
            right -= 1


# Example usage:
numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))  # Output: [1, 2]
