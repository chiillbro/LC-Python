class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0

        res = 0

        for right in range(n):
            if nums[right] == 0:
                continue 
            
            while nums[left] != 0 and left < right:
                left += 1
            
            length = right - left
            if length > 0:
                res += (length * ( length + 1 )) >> 1
                left = right
        
        if left == 0 and nums[0] == 0:
            return (n * (n + 1)) >> 1
        
        length = (n-1) - left
        res += (length * ( length + 1 )) >> 1
        
        return res