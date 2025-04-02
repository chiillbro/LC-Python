class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_value = 0

        # ** Brute Force ** TC: O(n^3) ** #
        # for i in range(len(nums) - 2):
        #     for j in range(i+1, len(nums) - 1):
        #         diff = nums[i] - nums[j]
        #         if diff < 0:
        #             continue
        #         for k in range(j+1, len(nums)):
        #             max_value = max(max_value, diff * nums[k])

        # ** Greedy Approach ** TC: O(n^2) ** #

        for k in range(2, len(nums)):
            max_prefix = nums[0]
            for j in range(1, k):
                max_value = max(max_value, (max_prefix - nums[j]) * nums[k])
                max_prefix = max(max_prefix, nums[j])

        return max_value
