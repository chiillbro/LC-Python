class Solution:
    def sliding_window_atmost(self, nums, k):
        n = len(nums)

        left = res = 0

        odds = 0

        for right in range(n):
            odds += nums[right] & 1

            while left <= right and odds > k:
                odds -= nums[left] & 1
                left += 1
            
            # if odds == k:
            res += (right - left + 1)
        
        return res
        
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Sliding Window Approach using "At Most" Trick
        # return self.sliding_window_atmost(nums, k) - self.sliding_window_atmost(nums, k - 1)

        # Standard and fundamental prefix sum using hashing approach
        n = len(nums)

        res = current_sum = 0

        prefix_map = defaultdict(int)
        prefix_map[0] = 1

        for num in nums:
            current_sum += num & 1

            prefix_sum_needed = current_sum - k
            if prefix_sum_needed in prefix_map:
                res += prefix_map[prefix_sum_needed]
            
            prefix_map[current_sum] += 1
        
        return res