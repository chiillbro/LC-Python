class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)

        zeroes = 0
        res = left = 0

        for right in range(n):
            if nums[right] == 0:
                zeroes += 1
            
            if left <= right and zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            res = max(res, right - left + 1)
        
        return res