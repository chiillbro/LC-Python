class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0

        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                diff = nums[i] - nums[j]
                if diff < 0:
                    continue
                for k in range(j+1, len(nums)):
                    max_value = max(max_value, diff * nums[k])

        return max_value
