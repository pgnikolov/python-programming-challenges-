class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage:
height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))  # Output: 49
