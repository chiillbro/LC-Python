class Solution:
    def sliding_window_atmost(self, nums, k):
        n = len(nums)

        left = res = 0

        odds = 0

        for right in range(n):
            if nums[right] & 1:
                odds += 1
            

            while left <= right and odds > k:
                if nums[left] & 1:
                    odds -= 1
                
                left += 1
            
            # if odds == k:
            res += (right - left + 1)
        
        return res
        
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.sliding_window_atmost(nums, k) - self.sliding_window_atmost(nums, k - 1)