class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return 0

        total = 0

        for i in range(1, n-1):
            if nums[i] == nums[i-1]: continue
            j, k = i-1, i+1

            while j >= 0 and nums[j] == nums[i]:
                j -= 1
            
            while k < n and nums[k] == nums[i]:
                k += 1
            
            if j < 0  or k >= n:
                continue
            
            is_hill = nums[j] < nums[i] and nums[k] < nums[i]

            is_valley = nums[j] > nums[i] and nums[k] > nums[i]

            if is_hill or is_valley:
                total += 1
        
        return total