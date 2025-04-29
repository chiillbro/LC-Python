class Solution:
    def sliding_window_at_most(self, nums: list[int], goal: int) -> int:
        n = len(nums)

        ones = 0
        left = res = 0

        for right in range(n):
            ones += nums[right]
            
            while left <= right and ones > goal:
                ones -= nums[left]
                
                left += 1
            
            res += right - left + 1
        
        return res

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)