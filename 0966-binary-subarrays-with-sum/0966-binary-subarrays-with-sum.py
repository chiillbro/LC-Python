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
    #     return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)
        n = len(nums)
        res = 0

        current_sum = 0

        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1

        for num in nums:
            current_sum += num

            needed_prefix_sum = current_sum - goal

            if needed_prefix_sum in prefix_sum_counts:
                res += prefix_sum_counts[needed_prefix_sum]
            
            prefix_sum_counts[current_sum] += 1
        
        return res