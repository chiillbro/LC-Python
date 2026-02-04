class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 4:
            return False
        

        if nums[1] <= nums[0]: return False

        if nums[-1] <= nums[-2]: return False


        i = 1

        while i < n and nums[i] > nums[i-1]:
            i += 1

        if i == n:
            return False
        
        j = i
        while i < n and nums[i] < nums[i-1]:
            i += 1

        if i == j or i == n:
            return False
        
        while i < n and nums[i] > nums[i-1]:
            i += 1
        
        if i != n:
            return False

        
        return True