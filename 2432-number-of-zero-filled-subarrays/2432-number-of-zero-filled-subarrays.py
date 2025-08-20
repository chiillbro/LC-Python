class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # left = 0

        # res = 0

        # for right in range(n):
        #     if nums[right] == 0:
        #         continue 
            
        #     while nums[left] != 0 and left < right:
        #         left += 1
            
        #     length = right - left
        #     if length > 0:
        #         res += (length * ( length + 1 )) >> 1
        #         left = right
        
        # if left == 0 and nums[0] == 0:
        #     return (n * (n + 1)) >> 1
        
        # length = (n-1) - left
        # res += (length * ( length + 1 )) >> 1
        
        # return res

        # PREFERRED APPROACH
        # zeroes_streak = res = 0

        # for i in range(n):
        #     if nums[i] == 0:
        #         zeroes_streak += 1
        #     else:
        #         res += (zeroes_streak * (zeroes_streak + 1)) >> 1

        #         zeroes_streak = 0
        
        # if zeroes_streak > 0:
        #     res += (zeroes_streak * (zeroes_streak + 1)) >> 1
    
        # return res


        # PYTHONIC WAY
        res = 0

        for key, group in groupby(nums): # groupby groups consecutive identical elements
            if key == 0: # we only care about '0's
                length = len(list(group))
                res += (length * ( length + 1 )) >> 1
        
        return res