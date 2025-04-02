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
        
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = max(prefix_sum[i-1], nums[i - 1])
            suffix_sum[n - 1 - i] = max(suffix_sum[n - i], nums[n - i])
        
        for j in range(1, n-1):
            max_value = max(max_value, (prefix_sum[j] - nums[j]) * suffix_sum[j])

        return max_value
