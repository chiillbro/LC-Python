class Solution:
    def maxSum(self, nums: List[int]) -> int:
        sub_sum = sum(num for num in set(nums) if num > 0)

        if not sub_sum:
            return max(nums)
        
        return sub_sum