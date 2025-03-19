class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0

        for i in range(2, len(nums)):
            if not nums[i-2]:
                count += 1
                nums[i-2] ^= 1
                nums[i-1] ^= 1
                nums[i] ^= 1

        return count if sum(nums) == len(nums) else -1