class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        most = 0

        left = 0
        right = len(heights) - 1

        while left < right:

            height = min(heights[left], heights[right])

            water = height * (right - left)

            most = max(most, water)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return most