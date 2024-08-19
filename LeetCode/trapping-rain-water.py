def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] < left_max:
                water_trapped += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if height[right] < right_max:
                water_trapped += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1

    return water_trapped


height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height2 = [4, 2, 0, 3, 2, 5]

print(trap(height1))  # Output: 6
print(trap(height2))  # Output: 9