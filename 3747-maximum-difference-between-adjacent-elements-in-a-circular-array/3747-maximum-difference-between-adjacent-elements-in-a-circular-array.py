class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        # nums: int[]
        # to find the absolute difference between adj elem

        _max = float('-inf')
        i = -1
        n = len(nums)

        while i < n-1:
            _max = max(_max, abs(nums[i] - nums[i+1]))
            i += 1
        
        return _max