class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0

        # ** Brute Force ** TC: O(n^3) ** #
        # for i in range(n - 2):
        #     for j in range(i+1, n - 1):
        #         diff = nums[i] - nums[j]
        #         if diff < 0:
        #             continue
        #         for k in range(j+1, n):
        #             max_value = max(max_value, diff * nums[k])

        # ** Greedy Approach ** TC: O(n^2) ** #

        # for k in range(2, n):
        #     max_prefix = nums[0]
        #     for j in range(1, k):
        #         max_value = max(max_value, (max_prefix - nums[j]) * nums[k])
        #         max_prefix = max(max_prefix, nums[j])

        # ** Greedy + prefix Suffix Array ** TC: O(n) #
        
        left_max = [0] * n
        right_max = [0] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], nums[i - 1])
            right_max[n - 1 - i] = max(right_max[n - i], nums[n - i])
        
        for j in range(1, n-1):
            max_value = max(max_value, (left_max[j] - nums[j]) * right_max[j])

        return max_value
