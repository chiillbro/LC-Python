class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, max_area = 0, len(height) - 1, 0

        while left < right:
            width = right - left
            cur_area = min(height[left], height[right]) * width
            max_area = max(cur_area, max_area)
            if height[left] < height[right]: left += 1
            else: right -= 1
        
        return max_area