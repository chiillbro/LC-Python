class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        res = 0
        left = 0
        _sum = 0
        for right in range(n):
            _sum += nums[right]

            while left <= right and _sum * (right - left + 1) >= k:
                _sum -= nums[left]
                left += 1
            
            res += (right - left + 1)
        
        return res