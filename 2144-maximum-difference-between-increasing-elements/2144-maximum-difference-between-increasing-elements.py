class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # nums: int[]
        # brute force:
        n = len(nums)

        _max_diff = -1
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    _max_diff = max(_max_diff, nums[j] - nums[i])
    
        return _max_diff
