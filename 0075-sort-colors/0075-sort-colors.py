class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zeroes = ones = twos = 0

        for num in nums:
            if not num:
                zeroes += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        
        i = 0
        while zeroes:
            nums[i] = 0
            i += 1
            zeroes -= 1
        
        while ones:
            nums[i] = 1
            i += 1
            ones -= 1
        while twos:
            nums[i] = 2
            i += 1
            twos -= 1
    