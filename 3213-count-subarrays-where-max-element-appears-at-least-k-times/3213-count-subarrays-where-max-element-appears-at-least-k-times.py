class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_ele = max(nums)

        res = left = 0
        max_ele_count = 0

        for right in range(n):
            if nums[right] == max_ele:
                max_ele_count += 1
            
            while max_ele_count == k:
                if nums[left] == max_ele:
                    max_ele_count -= 1
                
                left += 1
            
            res += left
        
        return res